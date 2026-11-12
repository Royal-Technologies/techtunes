"""Master Synchronization Engine for Techtunes Archive.

Supports both full/seed import and daily incremental synchronization from
https://www.techtunes.io/ with revision history tracking, media downloading,
Markdown generation, and JSON export pipelines.
"""

from __future__ import annotations

import argparse
import html
import json
import logging
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import (
    checkpoint_and_clean_db,
    compute_content_hash,
    get_db,
    init_database,
    utc_now_iso,
)
from scripts.json_export import generate_json_exports
from scripts.markdown_export import (
    determine_article_path,
    detect_language,
    html_to_clean_markdown,
    save_article_markdown,
)
from scripts.media import MediaArchiver
from scripts.search_index import build_search_indexes
from scripts.techtunes import TechtunesClient, stable_int_id

LOGS_DIR = ROOT_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR = ROOT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOGS_DIR / f"sync_{datetime.now(timezone.utc).strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(str(log_file), encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("archive.sync")


def load_sources_config() -> List[Dict[str, Any]]:
    """Loads sources from config/sources.json."""
    config_file = ROOT_DIR / "config" / "sources.json"
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f).get("sources", [])


def load_settings() -> Dict[str, Any]:
    """Loads runtime settings from config/settings.json."""
    settings_file = ROOT_DIR / "config" / "settings.json"
    if settings_file.exists():
        with open(settings_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class ArchiveSynchronizer:
    """Orchestrates ingestion, persistence, and exports for Techtunes."""

    def __init__(
        self,
        mode: str = "incremental",
        target_source: Optional[str] = None,
        max_pages: Optional[int] = None,
        max_posts: Optional[int] = None,
    ) -> None:
        self.mode = mode
        self.target_source = target_source
        self.max_pages = max_pages
        self.max_posts = max_posts
        self.settings = load_settings()
        self.media_archiver = MediaArchiver()
        init_database()

    def _upsert_author(self, conn: Any, site_id: int, author_data: Dict[str, Any]) -> int:
        now = utc_now_iso()
        wp_author_id = author_data.get("id") or stable_int_id(f"author:{author_data.get('slug', 'tuner')}")
        name = html.unescape(author_data.get("name") or "Techtunes Tuner").strip()
        slug = author_data.get("slug") or "tuner"
        url = author_data.get("url") or ""
        avatar_url = author_data.get("avatar_url") or ""
        desc = author_data.get("description") or ""

        conn.execute(
            """
            INSERT INTO authors (site_id, wp_author_id, name, slug, url, description, avatar_url, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(site_id, wp_author_id) DO UPDATE SET
                name = excluded.name,
                slug = excluded.slug,
                url = CASE WHEN excluded.url != '' THEN excluded.url ELSE authors.url END,
                avatar_url = CASE WHEN excluded.avatar_url != '' THEN excluded.avatar_url ELSE authors.avatar_url END,
                updated_at = excluded.updated_at
            """,
            (site_id, wp_author_id, name, slug, url, desc, avatar_url, now, now),
        )
        row = conn.execute(
            "SELECT id FROM authors WHERE site_id = ? AND wp_author_id = ?",
            (site_id, wp_author_id),
        ).fetchone()
        return row["id"]

    def _upsert_category(self, conn: Any, site_id: int, cat_data: Dict[str, Any]) -> int:
        now = utc_now_iso()
        wp_cat_id = cat_data.get("id") or stable_int_id(f"cat:{cat_data.get('slug', 'general')}")
        name = html.unescape(cat_data.get("name") or "General").strip()
        slug = cat_data.get("slug") or "general"
        desc = cat_data.get("description") or ""

        conn.execute(
            """
            INSERT INTO categories (site_id, wp_category_id, name, slug, description, parent_id, count, created_at)
            VALUES (?, ?, ?, ?, ?, 0, 0, ?)
            ON CONFLICT(site_id, wp_category_id) DO UPDATE SET
                name = excluded.name,
                slug = excluded.slug
            """,
            (site_id, wp_cat_id, name, slug, desc, now),
        )
        row = conn.execute(
            "SELECT id FROM categories WHERE site_id = ? AND wp_category_id = ?",
            (site_id, wp_cat_id),
        ).fetchone()
        return row["id"]

    def _upsert_tag(self, conn: Any, site_id: int, tag_data: Dict[str, Any]) -> int:
        now = utc_now_iso()
        wp_tag_id = tag_data.get("id") or stable_int_id(f"tag:{tag_data.get('name', 'tag')}")
        name = html.unescape(tag_data.get("name") or "Tag").strip()
        slug = tag_data.get("slug") or "tag"

        conn.execute(
            """
            INSERT INTO tags (site_id, wp_tag_id, name, slug, description, count, created_at)
            VALUES (?, ?, ?, ?, '', 0, ?)
            ON CONFLICT(site_id, wp_tag_id) DO UPDATE SET
                name = excluded.name,
                slug = excluded.slug
            """,
            (site_id, wp_tag_id, name, slug, now),
        )
        row = conn.execute(
            "SELECT id FROM tags WHERE site_id = ? AND wp_tag_id = ?",
            (site_id, wp_tag_id),
        ).fetchone()
        return row["id"]

    def sync_initial_categories(self, conn: Any, client: TechtunesClient, site_id: int, source_key: str) -> None:
        """Pre-populates official Techtunes categories from homepage directory."""
        logger.info(f"[{source_key}] Syncing official categories...")
        categories = client.get_categories()
        for c in categories:
            self._upsert_category(conn, site_id, c)

    def process_featured_media(
        self,
        conn: Any,
        site_id: int,
        source_key: str,
        image_url: Optional[str],
        title: str = "",
    ) -> Optional[int]:
        """Archives featured image for a tune if present."""
        if not image_url:
            return None

        wp_media_id = stable_int_id(f"media:{image_url}")
        existing = conn.execute(
            "SELECT id, local_path, download_status FROM media WHERE site_id = ? AND wp_media_id = ?",
            (site_id, wp_media_id),
        ).fetchone()
        if existing and existing["download_status"] == "completed" and existing["local_path"]:
            return existing["id"]

        download_res = self.media_archiver.download_image(image_url, source_key)
        now = utc_now_iso()

        conn.execute(
            """
            INSERT INTO media (
                site_id, wp_media_id, original_url, local_path, file_name,
                mime_type, file_size, sha256_hash, alt_text, caption,
                download_status, downloaded_at, error_message, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, '', ?, ?, ?, ?)
            ON CONFLICT(site_id, wp_media_id) DO UPDATE SET
                local_path = excluded.local_path,
                download_status = excluded.download_status,
                downloaded_at = excluded.downloaded_at,
                error_message = excluded.error_message
            """,
            (
                site_id,
                wp_media_id,
                image_url,
                download_res.get("local_path"),
                Path(download_res.get("local_path", "")).name if download_res.get("local_path") else None,
                download_res.get("mime_type"),
                download_res.get("file_size", 0),
                download_res.get("sha256_hash"),
                title,
                download_res.get("status", "failed"),
                now if download_res.get("status") == "completed" else None,
                download_res.get("error_message"),
                now,
            ),
        )
        row = conn.execute(
            "SELECT id FROM media WHERE site_id = ? AND wp_media_id = ?",
            (site_id, wp_media_id),
        ).fetchone()
        return row["id"] if row else None

    def sync_single_source(self, source_conf: Dict[str, Any]) -> Dict[str, Any]:
        """Performs full or incremental sync for Techtunes."""
        source_key = source_conf["key"]
        source_name = source_conf["name"]
        default_lang = source_conf.get("default_language", "bn")

        sync_stats = {
            "source_key": source_key,
            "source_name": source_name,
            "mode": self.mode,
            "status": "success",
            "posts_created": 0,
            "posts_updated": 0,
            "posts_unchanged": 0,
            "media_downloaded": 0,
            "errors_count": 0,
            "error_details": [],
            "started_at": utc_now_iso(),
            "finished_at": None,
        }

        logger.info(f"[{source_key}] Starting sync (mode: {self.mode})...")

        sync_cfg = self.settings.get("sync", {})
        client = TechtunesClient(
            base_url=source_conf["base_url"],
            feed_url=source_conf.get("api_url", f"{source_conf['base_url']}/feed/"),
            source_key=source_key,
            timeout=sync_cfg.get("request_timeout_seconds", 30),
            max_retries=sync_cfg.get("max_retries", 3),
            retry_backoff=sync_cfg.get("retry_backoff_factor", 1.5),
            delay_ms=sync_cfg.get("delay_between_requests_ms", 200),
        )

        with get_db() as conn:
            site_row = conn.execute("SELECT id FROM sites WHERE key = ?", (source_key,)).fetchone()
            if not site_row:
                raise ValueError(f"Site key {source_key} not registered in database.")
            site_id = site_row["id"]

            conn.execute(
                "UPDATE sync_state SET sync_status = 'running', updated_at = ? WHERE site_id = ?",
                (utc_now_iso(), site_id),
            )

            try:
                self.sync_initial_categories(conn, client, site_id, source_key)

                modified_after = None
                if self.mode == "incremental":
                    state_row = conn.execute(
                        "SELECT last_post_modified_at FROM sync_state WHERE site_id = ?",
                        (site_id,),
                    ).fetchone()
                    if state_row and state_row["last_post_modified_at"]:
                        overlap_hours = sync_cfg.get("overlap_hours", 48)
                        try:
                            last_mod = datetime.fromisoformat(
                                state_row["last_post_modified_at"].replace("Z", "+00:00")
                            )
                            cutoff = last_mod - timedelta(hours=overlap_hours)
                            modified_after = cutoff.isoformat()
                            logger.info(f"[{source_key}] Incremental cutoff window: {modified_after}")
                        except Exception as e:
                            logger.warning(f"[{source_key}] Could not parse last modified date: {e}")

                default_pages = (
                    sync_cfg.get("full_max_pages", 3)
                    if self.mode == "full"
                    else sync_cfg.get("incremental_max_pages", 5)
                )
                effective_max_pages = self.max_pages if self.max_pages is not None else default_pages
                include_homepage = sync_cfg.get("include_homepage", True)
                include_sitemap = sync_cfg.get("include_sitemap_recent", 60)

                latest_post_modified: Optional[str] = None

                for tune in client.iterate_tunes(
                    mode=self.mode,
                    max_pages=effective_max_pages,
                    modified_after=modified_after,
                    include_homepage=include_homepage,
                    include_sitemap_recent=include_sitemap,
                    max_posts=self.max_posts,
                ):
                    tune_id = tune["id"]
                    archive_id = f"{source_key}-{tune_id}"

                    title = tune["title"]
                    raw_html = tune.get("content_html") or ""
                    clean_excerpt = tune.get("excerpt") or ""
                    slug = tune.get("slug") or f"tune-{tune_id}"
                    original_url = tune["url"]
                    published_at = tune.get("published_at") or utc_now_iso()
                    modified_at = tune.get("modified_at") or published_at

                    if not latest_post_modified or modified_at > latest_post_modified:
                        latest_post_modified = modified_at

                    markdown_body = html_to_clean_markdown(raw_html)
                    if not markdown_body:
                        markdown_body = clean_excerpt or "*(No textual body content was available for this tune.)*"

                    language = detect_language(title, markdown_body, default_language=default_lang)
                    content_hash = compute_content_hash(f"{title}\n{markdown_body}")

                    author_info = tune.get("author") or {"name": "Techtunes Community", "slug": "techtunes"}
                    db_author_id = self._upsert_author(conn, site_id, author_info)

                    cat_ids: List[int] = []
                    cat_names: List[str] = []
                    for c in tune.get("categories", []):
                        cid = self._upsert_category(conn, site_id, c)
                        cat_ids.append(cid)
                        cat_names.append(c["name"])

                    tag_ids: List[int] = []
                    tag_names: List[str] = []
                    for t in tune.get("tags", []):
                        tid = self._upsert_tag(conn, site_id, t)
                        tag_ids.append(tid)
                        tag_names.append(t["name"])

                    db_media_id = self.process_featured_media(
                        conn, site_id, source_key, tune.get("featured_image_url"), title=title
                    )
                    if db_media_id:
                        sync_stats["media_downloaded"] += 1

                    existing = conn.execute(
                        "SELECT id, title, content_html, content_markdown, excerpt, modified_at, "
                        "modified_at_gmt, content_hash, markdown_path "
                        "FROM posts WHERE site_id = ? AND wp_post_id = ?",
                        (site_id, tune_id),
                    ).fetchone()

                    now = utc_now_iso()

                    if existing is None:
                        md_path = determine_article_path(
                            source_key=source_key,
                            language=language,
                            published_at=published_at,
                            slug=slug,
                            wp_post_id=tune_id,
                        )
                        rel_md_path = str(md_path.relative_to(ROOT_DIR)).replace("\\", "/")

                        conn.execute(
                            """
                            INSERT INTO posts (
                                archive_id, site_id, wp_post_id, title, slug, language,
                                content_html, content_markdown, excerpt, status, post_type,
                                original_url, published_at, published_at_gmt, modified_at,
                                modified_at_gmt, author_id, featured_media_id, content_hash,
                                markdown_path, archived_at, created_at, updated_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'publish', 'post', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                archive_id, site_id, tune_id, title, slug, language,
                                raw_html, markdown_body, clean_excerpt, original_url,
                                published_at, published_at, modified_at, modified_at,
                                db_author_id, db_media_id, content_hash, rel_md_path,
                                now, now, now,
                            ),
                        )
                        post_db_id = conn.execute(
                            "SELECT id FROM posts WHERE archive_id = ?", (archive_id,)
                        ).fetchone()["id"]

                        for cid in cat_ids:
                            conn.execute(
                                "INSERT OR IGNORE INTO post_categories (post_id, category_id) VALUES (?, ?)",
                                (post_db_id, cid),
                            )
                        for tid in tag_ids:
                            conn.execute(
                                "INSERT OR IGNORE INTO post_tags (post_id, tag_id) VALUES (?, ?)",
                                (post_db_id, tid),
                            )

                        meta = {
                            "archive_id": archive_id,
                            "source": source_key,
                            "source_name": source_name,
                            "wordpress_id": tune_id,
                            "title": title,
                            "slug": slug,
                            "language": language,
                            "status": "publish",
                            "published_at": published_at,
                            "modified_at": modified_at,
                            "original_url": original_url,
                            "author": author_info.get("name", "Techtunes Community"),
                            "author_url": author_info.get("url", ""),
                            "categories": cat_names,
                            "tags": tag_names,
                            "content_hash": content_hash,
                            "archived_at": now,
                        }
                        save_article_markdown(md_path, meta, markdown_body)
                        sync_stats["posts_created"] += 1
                        logger.info(f"[{source_key}] [+] Created: {archive_id} - {title[:60]}")

                    else:
                        post_db_id = existing["id"]
                        old_hash = existing["content_hash"]

                        if old_hash != content_hash:
                            rev_count = conn.execute(
                                "SELECT count(*) as c FROM post_revisions WHERE post_id = ?",
                                (post_db_id,),
                            ).fetchone()["c"]
                            next_rev = rev_count + 1

                            conn.execute(
                                """
                                INSERT INTO post_revisions (
                                    post_id, revision_number, title, content_html,
                                    content_markdown, excerpt, modified_at, modified_at_gmt,
                                    content_hash, change_summary, recorded_at
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Synchronized update from Techtunes', ?)
                                """,
                                (
                                    post_db_id, next_rev, existing["title"],
                                    existing["content_html"], existing["content_markdown"],
                                    existing["excerpt"], existing["modified_at"],
                                    existing["modified_at_gmt"], old_hash, now,
                                ),
                            )

                            conn.execute(
                                """
                                UPDATE posts SET
                                    title = ?,
                                    content_html = ?,
                                    content_markdown = ?,
                                    excerpt = ?,
                                    language = ?,
                                    modified_at = ?,
                                    modified_at_gmt = ?,
                                    content_hash = ?,
                                    author_id = ?,
                                    featured_media_id = ?,
                                    updated_at = ?
                                WHERE id = ?
                                """,
                                (
                                    title, raw_html, markdown_body, clean_excerpt,
                                    language, modified_at, modified_at, content_hash,
                                    db_author_id, db_media_id, now, post_db_id,
                                ),
                            )

                            conn.execute("DELETE FROM post_categories WHERE post_id = ?", (post_db_id,))
                            for cid in cat_ids:
                                conn.execute(
                                    "INSERT OR IGNORE INTO post_categories (post_id, category_id) VALUES (?, ?)",
                                    (post_db_id, cid),
                                )
                            conn.execute("DELETE FROM post_tags WHERE post_id = ?", (post_db_id,))
                            for tid in tag_ids:
                                conn.execute(
                                    "INSERT OR IGNORE INTO post_tags (post_id, tag_id) VALUES (?, ?)",
                                    (post_db_id, tid),
                                )

                            md_full_path = ROOT_DIR / existing["markdown_path"]
                            meta = {
                                "archive_id": archive_id,
                                "source": source_key,
                                "source_name": source_name,
                                "wordpress_id": tune_id,
                                "title": title,
                                "slug": slug,
                                "language": language,
                                "status": "publish",
                                "published_at": published_at,
                                "modified_at": modified_at,
                                "original_url": original_url,
                                "author": author_info.get("name", "Techtunes Community"),
                                "author_url": author_info.get("url", ""),
                                "categories": cat_names,
                                "tags": tag_names,
                                "content_hash": content_hash,
                                "archived_at": now,
                            }
                            save_article_markdown(md_full_path, meta, markdown_body)
                            sync_stats["posts_updated"] += 1
                            logger.info(f"[{source_key}] [*] Updated (rev {next_rev}): {archive_id} - {title[:60]}")
                        else:
                            sync_stats["posts_unchanged"] += 1

                finish_time = utc_now_iso()
                sync_stats["finished_at"] = finish_time

                total_synced = conn.execute(
                    "SELECT count(*) as c FROM posts WHERE site_id = ?", (site_id,)
                ).fetchone()["c"]

                conn.execute(
                    """
                    UPDATE sync_state SET
                        last_sync_at = ?,
                        last_post_modified_at = coalesce(?, last_post_modified_at),
                        total_synced_posts = ?,
                        sync_status = 'success',
                        error_message = NULL,
                        updated_at = ?
                    WHERE site_id = ?
                    """,
                    (finish_time, latest_post_modified, total_synced, finish_time, site_id),
                )

                conn.execute(
                    """
                    INSERT INTO sync_logs (
                        site_id, mode, started_at, finished_at, status,
                        posts_created, posts_updated, posts_unchanged,
                        media_downloaded, errors_count, details_json
                    ) VALUES (?, ?, ?, ?, 'success', ?, ?, ?, ?, 0, ?)
                    """,
                    (
                        site_id, self.mode, sync_stats["started_at"], finish_time,
                        sync_stats["posts_created"], sync_stats["posts_updated"],
                        sync_stats["posts_unchanged"], sync_stats["media_downloaded"],
                        json.dumps(sync_stats, ensure_ascii=False),
                    ),
                )

            except Exception as e:
                err_time = utc_now_iso()
                sync_stats["status"] = "error"
                sync_stats["finished_at"] = err_time
                sync_stats["errors_count"] += 1
                sync_stats["error_details"].append(str(e))
                logger.error(f"[{source_key}] Sync error: {e}", exc_info=True)

                conn.execute(
                    """
                    UPDATE sync_state SET
                        sync_status = 'error',
                        error_message = ?,
                        updated_at = ?
                    WHERE site_id = ?
                    """,
                    (str(e), err_time, site_id),
                )

                conn.execute(
                    """
                    INSERT INTO sync_logs (
                        site_id, mode, started_at, finished_at, status,
                        posts_created, posts_updated, posts_unchanged,
                        media_downloaded, errors_count, details_json
                    ) VALUES (?, ?, ?, ?, 'error', ?, ?, ?, ?, 1, ?)
                    """,
                    (
                        site_id, self.mode, sync_stats["started_at"], err_time,
                        sync_stats["posts_created"], sync_stats["posts_updated"],
                        sync_stats["posts_unchanged"], sync_stats["media_downloaded"],
                        json.dumps(sync_stats, ensure_ascii=False),
                    ),
                )

        return sync_stats

    def run(self) -> List[Dict[str, Any]]:
        """Executes synchronization according to configuration and arguments."""
        sources = load_sources_config()
        all_stats = []

        for src in sources:
            if not src.get("enabled", True):
                continue
            if self.target_source and src["key"] != self.target_source:
                continue

            stats = self.sync_single_source(src)
            all_stats.append(stats)

        with get_db() as conn:
            logger.info("Generating deterministic JSON exports...")
            generate_json_exports(conn)
            logger.info("Building static search indexes...")
            build_search_indexes(conn)

        checkpoint_and_clean_db()

        report_file = REPORTS_DIR / f"sync_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w", encoding="utf-8") as rf:
            json.dump(all_stats, rf, ensure_ascii=False, indent=2)

        logger.info(f"Sync complete. Report saved to {report_file}")
        return all_stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize Techtunes Archive from techtunes.io")
    parser.add_argument(
        "--mode",
        choices=["full", "incremental"],
        default="incremental",
        help="Synchronization mode: full or daily incremental",
    )
    parser.add_argument(
        "--source",
        choices=["techtunes"],
        default=None,
        help="Restrict sync to a specific source",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Maximum RSS feed pages to scan (0 = unlimited)",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=None,
        help="Optional cap on maximum tunes fetched in one run",
    )
    args = parser.parse_args()

    syncer = ArchiveSynchronizer(
        mode=args.mode,
        target_source=args.source,
        max_pages=args.max_pages,
        max_posts=args.max_posts,
    )
    results = syncer.run()

    has_errors = any(r["status"] == "error" for r in results)
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
