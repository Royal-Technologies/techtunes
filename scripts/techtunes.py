"""Techtunes Content & Feed Client for Techtunes Archive.

Fetches official categories, RSS feeds, homepage/archive tune listings,
sitemap updates, and full tune HTML articles from https://www.techtunes.io/.
"""

from __future__ import annotations

import email.utils
import html
import logging
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import threading
from typing import Any, Dict, Generator, List, Optional, Set, Tuple

import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateutil_parser

logger = logging.getLogger("archive.techtunes")

TUNE_ID_PATTERN = re.compile(r"/tune-id/(\d+)")
POST_GUID_PATTERN = re.compile(r"[?&]p=(\d+)")
GENERIC_OG_IMAGE = "techtunes_9153c5aa40c6b4514820f0d12d0804af.jpg"


class TechtunesClientError(Exception):
    """Base exception for Techtunes scraping/feed interactions."""


def stable_int_id(value: str) -> int:
    """Computes a deterministic positive 31-bit integer ID from a string."""
    digest = zlib.crc32((value or "default").encode("utf-8")) & 0x7FFFFFFF
    return digest if digest > 0 else 1


def parse_iso_datetime(value: Optional[str]) -> Optional[datetime]:
    """Parses ISO 8601 or RFC 2822 datetime string into timezone-aware UTC datetime."""
    if not value:
        return None
    try:
        dt = dateutil_parser.parse(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def make_soup(markup: str) -> BeautifulSoup:
    """Creates a BeautifulSoup tree preferring lxml with html.parser fallback."""
    try:
        return BeautifulSoup(markup, "lxml")
    except Exception:
        return BeautifulSoup(markup, "html.parser")


def extract_tune_id(url: str, guid: str = "") -> Optional[int]:
    """Extracts numeric Techtunes tune ID from URL or RSS guid."""
    for candidate in (url, guid):
        if not candidate:
            continue
        m = TUNE_ID_PATTERN.search(candidate)
        if m:
            return int(m.group(1))
        m2 = POST_GUID_PATTERN.search(candidate)
        if m2:
            return int(m2.group(1))
    return None


def extract_category_slug_from_url(url: str) -> str:
    """Extracts category slug from URL like https://www.techtunes.io/tips-and-tricks/tune-id/1024973."""
    parsed = urllib.parse.urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 3 and parts[-2] == "tune-id":
        return parts[0]
    if "/category/" in parsed.path:
        return parsed.path.rstrip("/").split("/")[-1]
    return "general"


class TechtunesClient:
    """Resilient HTTP client for ingesting content from https://www.techtunes.io/."""

    def __init__(
        self,
        base_url: str = "https://www.techtunes.io",
        feed_url: str = "https://www.techtunes.io/feed/",
        source_key: str = "techtunes",
        timeout: int = 30,
        max_retries: int = 3,
        retry_backoff: float = 1.5,
        delay_ms: int = 200,
        user_agent: Optional[str] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.feed_url = feed_url.rstrip("/")
        self.source_key = source_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        self.delay_seconds = max(0.0, delay_ms / 1000.0)

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent or (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36 TechtunesArchive/1.0"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "bn-BD,bn;q=0.9,en-US;q=0.8,en;q=0.7",
        })
        self._thread_local = threading.local()

    def _get_session(self) -> requests.Session:
        """Returns main session on main thread and thread-local session on workers."""
        if threading.current_thread() is threading.main_thread():
            return self.session
        sess = getattr(self._thread_local, "session", None)
        if sess is None:
            sess = requests.Session()
            sess.headers.update(self.session.headers)
            self._thread_local.session = sess
        return sess

    def _request(self, url: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Executes GET request with throttling and exponential backoff retries."""
        full_url = url if url.startswith("http") else f"{self.base_url}/{url.lstrip('/')}"
        if self.delay_seconds > 0:
            time.sleep(self.delay_seconds)

        last_exception: Optional[Exception] = None
        current_delay = 1.0
        session = self._get_session()

        for attempt in range(1, self.max_retries + 1):
            try:
                resp = session.get(full_url, params=params, timeout=self.timeout)
                if resp.status_code in (429, 500, 502, 503, 504):
                    logger.warning(
                        f"[{self.source_key}] HTTP {resp.status_code} for {full_url}. "
                        f"Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= self.retry_backoff
                    continue
                if 400 <= resp.status_code < 500:
                    resp.raise_for_status()
                resp.raise_for_status()
                return resp
            except requests.HTTPError as e:
                if e.response is not None and 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    raise TechtunesClientError(f"HTTP {e.response.status_code} for {full_url}") from e
                last_exception = e
            except (requests.RequestException, ConnectionError, TimeoutError) as e:
                last_exception = e
                logger.warning(
                    f"[{self.source_key}] Request error ({type(e).__name__}: {e}) for {full_url}. "
                    f"Attempt {attempt}/{self.max_retries}"
                )
            if attempt == self.max_retries:
                break
            time.sleep(current_delay)
            current_delay *= self.retry_backoff

        raise TechtunesClientError(
            f"Failed to fetch {full_url} after {self.max_retries} attempts: {last_exception}"
        ) from last_exception

    def get_categories(self) -> List[Dict[str, Any]]:
        """Extracts official Techtunes categories from the homepage category modal."""
        try:
            resp = self._request(f"{self.base_url}/")
            soup = make_soup(resp.text)
            modal = soup.find(id="all-tune-category-modal") or soup
            seen_slugs = set()
            categories: List[Dict[str, Any]] = []

            for a in modal.select('a[href*="/category/"]'):
                href = (a.get("href") or "").strip()
                name = html.unescape(a.get_text(" ", strip=True)).strip()
                if not href or not name:
                    continue
                slug = urllib.parse.urlparse(href).path.rstrip("/").split("/")[-1]
                if not slug or slug in seen_slugs:
                    continue
                seen_slugs.add(slug)
                categories.append({
                    "id": stable_int_id(f"cat:{slug}"),
                    "name": name,
                    "slug": slug,
                    "url": urllib.parse.urljoin(self.base_url, href),
                })

            logger.info(f"[{self.source_key}] Discovered {len(categories)} official categories.")
            return categories
        except Exception as e:
            logger.warning(f"[{self.source_key}] Failed to load categories from homepage: {e}")
            return []

    def parse_rss_feed_page(self, page: int = 1) -> List[Dict[str, Any]]:
        """Fetches and parses one RSS feed page (/feed/?paged=N)."""
        params = {"paged": page} if page > 1 else None
        resp = self._request(f"{self.feed_url}/", params=params)
        root = ET.fromstring(resp.text)

        dc_ns = "{http://purl.org/dc/elements/1.1/}"
        items: List[Dict[str, Any]] = []

        for item in root.findall(".//item"):
            title = html.unescape((item.findtext("title") or "").lstrip("\ufeff")).strip()
            link = (item.findtext("link") or "").strip()
            guid = (item.findtext("guid") or "").strip()
            creator = html.unescape(item.findtext(f"{dc_ns}creator") or "").strip()
            pub_raw = (item.findtext("pubDate") or "").strip()
            desc_raw = (item.findtext("description") or "").strip()

            tune_id = extract_tune_id(link, guid)
            if not tune_id or not link:
                continue

            pub_iso = None
            if pub_raw:
                try:
                    dt = email.utils.parsedate_to_datetime(pub_raw)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    pub_iso = dt.astimezone(timezone.utc).isoformat()
                except Exception:
                    dt2 = parse_iso_datetime(pub_raw)
                    pub_iso = dt2.isoformat() if dt2 else None

            cats = [
                html.unescape(c.text.strip())
                for c in item.findall("category")
                if c.text and c.text.strip()
            ]
            excerpt = ""
            if desc_raw:
                excerpt = make_soup(desc_raw).get_text(" ", strip=True)
                excerpt = re.sub(r"\s+", " ", excerpt).strip()

            items.append({
                "tune_id": tune_id,
                "url": link,
                "title": title,
                "author_name": creator,
                "published_at": pub_iso,
                "rss_terms": cats,
                "excerpt": excerpt,
            })

        return items

    def discover_homepage_tunes(self) -> List[Dict[str, Any]]:
        """Discovers tune links listed on the Techtunes homepage."""
        try:
            resp = self._request(f"{self.base_url}/")
            soup = make_soup(resp.text)
            seen_ids = set()
            entries: List[Dict[str, Any]] = []

            for a in soup.select('a[href*="/tune-id/"]'):
                href = (a.get("href") or "").strip()
                if not href:
                    continue
                full_url = urllib.parse.urljoin(self.base_url, href).split("#")[0].split("?")[0]
                tune_id = extract_tune_id(full_url)
                if not tune_id or tune_id in seen_ids:
                    continue
                seen_ids.add(tune_id)
                title = html.unescape((a.get("title") or a.get_text(" ", strip=True) or "").lstrip("\ufeff")).strip()
                entries.append({
                    "tune_id": tune_id,
                    "url": full_url,
                    "title": title,
                    "author_name": "",
                    "published_at": None,
                    "rss_terms": [],
                    "excerpt": "",
                })
            return entries
        except Exception as e:
            logger.warning(f"[{self.source_key}] Homepage discovery failed: {e}")
            return []

    def discover_sitemap_tunes(self, limit: int = 60) -> List[Dict[str, Any]]:
        """Discovers recent tunes from sitemap.xml with lastmod timestamps."""
        if limit <= 0:
            return []
        try:
            resp = self._request(f"{self.base_url}/sitemap.xml")
            root = ET.fromstring(resp.text)
            ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
            entries: List[Dict[str, Any]] = []

            for url_el in root.findall(f".//{ns}url"):
                loc = (url_el.findtext(f"{ns}loc") or "").strip()
                lastmod = (url_el.findtext(f"{ns}lastmod") or "").strip()
                tune_id = extract_tune_id(loc)
                if not tune_id:
                    continue
                entries.append({
                    "tune_id": tune_id,
                    "url": loc,
                    "title": "",
                    "author_name": "",
                    "published_at": lastmod or None,
                    "lastmod": lastmod or None,
                    "rss_terms": [],
                    "excerpt": "",
                })

            # Sort newest lastmod / tune_id first
            entries.sort(key=lambda x: (x.get("lastmod") or "", x["tune_id"]), reverse=True)
            return entries[:limit]
        except Exception as e:
            logger.warning(f"[{self.source_key}] Sitemap discovery failed: {e}")
            return []

    def parse_tune_html(
        self,
        url: str,
        raw_html: str,
        rss_meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Parses a full Techtunes article HTML page into a normalized tune dictionary."""
        rss_meta = rss_meta or {}
        soup = make_soup(raw_html)

        tune_id = extract_tune_id(url) or rss_meta.get("tune_id") or stable_int_id(url)

        # 1. Title
        h2 = soup.select_one("h2.h2-responsive.text-white")
        title = ""
        if h2:
            title = html.unescape(h2.get_text(" ", strip=True).lstrip("\ufeff")).strip()
        if not title:
            og_title = soup.find("meta", property="og:title")
            if og_title and og_title.get("content"):
                title = html.unescape(og_title["content"].lstrip("\ufeff")).strip()
                title = re.sub(r"\s*\|\s*Techtunes.*$", "", title, flags=re.IGNORECASE).strip()
        if not title:
            title = rss_meta.get("title") or f"Tune #{tune_id}"

        # 2. Published & Modified timestamps
        pub_meta = soup.find("meta", property="article:published_time")
        mod_meta = soup.find("meta", property="article:modified_time")

        pub_dt = parse_iso_datetime(pub_meta.get("content") if pub_meta else None) or parse_iso_datetime(
            rss_meta.get("published_at")
        )
        mod_dt = parse_iso_datetime(mod_meta.get("content") if mod_meta else None) or pub_dt

        published_at = (pub_dt or datetime.now(timezone.utc)).isoformat()
        modified_at = (mod_dt or pub_dt or datetime.now(timezone.utc)).isoformat()

        # 3. Featured image
        featured_image_url: Optional[str] = None
        if h2:
            banner_row = h2.find_parent("div", class_="row")
            if banner_row:
                banner_img = banner_row.find("img")
                if banner_img:
                    cand = (banner_img.get("data-src") or banner_img.get("src") or "").strip()
                    if cand and not cand.startswith("data:image/"):
                        featured_image_url = cand
        if not featured_image_url:
            for og_img in soup.find_all("meta", property="og:image"):
                cand = (og_img.get("content") or "").strip()
                if cand and GENERIC_OG_IMAGE not in cand:
                    featured_image_url = cand
                    break

        # 4. Author (Tuner)
        author_box = soup.select_one("div.pt-4.pt-md-7.pb-10")
        author_name = ""
        author_url = ""
        author_slug = ""
        author_avatar = ""

        if author_box:
            author_link = author_box.select_one('a[rel="author"][href*="/tuner/"]') or author_box.select_one(
                'a[href*="/tuner/"]'
            )
            if author_link:
                author_name = html.unescape(author_link.get_text(" ", strip=True)).strip()
                author_url = urllib.parse.urljoin(self.base_url, author_link.get("href", ""))
                author_slug = urllib.parse.urlparse(author_url).path.rstrip("/").split("/")[-1]
            avatar_img = author_box.select_one("img.avatar")
            if avatar_img:
                cand_av = (avatar_img.get("data-src") or avatar_img.get("src") or "").strip()
                if cand_av and not cand_av.startswith("data:image/"):
                    author_avatar = cand_av

        if not author_name:
            author_name = rss_meta.get("author_name") or "Techtunes Tuner"
        if not author_slug:
            author_slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", author_name.lower()).strip("-") or f"tuner-{stable_int_id(author_name)}"
        if not author_url:
            author_url = f"{self.base_url}/tuner/{author_slug}"

        # 5. Primary Category & Tags
        primary_categories: List[Tuple[str, str]] = []
        cat_seen = set()
        for a in soup.select('div.card-body.pt-0 a[href*="/category/"]'):
            cname = html.unescape(a.get_text(" ", strip=True)).strip()
            chref = (a.get("href") or "").strip()
            cslug = urllib.parse.urlparse(chref).path.rstrip("/").split("/")[-1]
            if cname and cslug and cslug not in cat_seen:
                cat_seen.add(cslug)
                primary_categories.append((cname, cslug))

        if not primary_categories:
            url_cat_slug = extract_category_slug_from_url(url)
            rss_terms = rss_meta.get("rss_terms") or []
            if rss_terms:
                primary_categories.append((rss_terms[0], url_cat_slug))
            else:
                primary_categories.append((url_cat_slug.replace("-", " ").title(), url_cat_slug))

        primary_cat_names = {c[0] for c in primary_categories}
        tags: List[Tuple[str, str]] = []
        tag_seen = set()

        for a in soup.select('a[href*="/tag/"]'):
            tname = html.unescape(a.get_text(" ", strip=True)).strip()
            tslug = urllib.parse.urlparse(a.get("href") or "").path.rstrip("/").split("/")[-1]
            if tname and tname not in primary_cat_names and tname not in tag_seen:
                tag_seen.add(tname)
                tags.append((tname, tslug or f"tag-{stable_int_id(tname)}"))

        for term in rss_meta.get("rss_terms") or []:
            if term and term not in primary_cat_names and term not in tag_seen:
                tag_seen.add(term)
                tags.append((term, f"tag-{stable_int_id(term)}"))

        # 6. Main Article Body HTML
        body_div = soup.select_one("div.card-body.px-3.px-sm-4.mb-3")
        if not body_div:
            card = soup.select_one(".card.z-depth-1.casecade-up")
            if card:
                candidates = card.select("div.card-body")
                if candidates:
                    body_div = max(candidates, key=lambda d: len(d.get_text(strip=True)))

        clean_body_html = ""
        if body_div:
            # Work on a copy via fresh soup fragment
            body_soup = make_soup(str(body_div))
            root_el = body_soup.select_one("div.card-body") or body_soup

            # Remove ad containers, revive ins tags, scripts, styles
            for sel in [".techtunes-adx", ".adsbygoogle", "ins[data-revive-id]", "script", "style", "noscript"]:
                for el in root_el.select(sel):
                    parent = el.parent
                    el.decompose()
                    if (
                        parent
                        and parent.name == "div"
                        and parent is not root_el
                        and not parent.get_text(strip=True)
                        and not parent.find(["img", "iframe", "video"])
                    ):
                        parent.decompose()

            # Promote data-src on images
            for img in root_el.find_all("img"):
                data_src = (img.get("data-src") or img.get("data-lazy-src") or "").strip()
                if data_src:
                    img["src"] = data_src
                for attr in ("data-src", "data-lazy-src", "data-srcset"):
                    if attr in img.attrs:
                        del img.attrs[attr]
                src = (img.get("src") or "").strip()
                if src.startswith("data:image/svg+xml"):
                    img.decompose()

            clean_body_html = "".join(str(ch) for ch in root_el.contents).strip()

        # 7. Excerpt
        excerpt = rss_meta.get("excerpt") or ""
        if not excerpt and clean_body_html:
            plain = make_soup(clean_body_html).get_text(" ", strip=True)
            plain = re.sub(r"\s+", " ", plain).strip()
            excerpt = (plain[:277] + "...") if len(plain) > 280 else plain

        cat_slug = extract_category_slug_from_url(url)
        slug = f"{cat_slug}-{tune_id}"

        return {
            "id": tune_id,
            "title": title,
            "slug": slug,
            "url": url,
            "published_at": published_at,
            "modified_at": modified_at,
            "content_html": clean_body_html,
            "excerpt": excerpt,
            "featured_image_url": featured_image_url,
            "author": {
                "id": stable_int_id(f"author:{author_slug}"),
                "name": author_name,
                "slug": author_slug,
                "url": author_url,
                "avatar_url": author_avatar,
            },
            "categories": [
                {"id": stable_int_id(f"cat:{cslug}"), "name": cname, "slug": cslug}
                for cname, cslug in primary_categories
            ],
            "tags": [
                {"id": stable_int_id(f"tag:{tname}"), "name": tname, "slug": tslug}
                for tname, tslug in tags
            ],
        }

    def fetch_tune_detail(self, url: str, rss_meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Downloads and parses a single Techtunes article page."""
        resp = self._request(url)
        return self.parse_tune_html(url, resp.text, rss_meta=rss_meta)

    def iterate_tunes(
        self,
        mode: str = "incremental",
        max_pages: int = 5,
        modified_after: Optional[str] = None,
        include_homepage: bool = True,
        include_sitemap_recent: int = 60,
        max_posts: Optional[int] = None,
        skip_tune_ids: Optional[Set[int]] = None,
        workers: int = 1,
    ) -> Generator[Dict[str, Any], None, None]:
        """Discovers and yields parsed Techtunes articles from feeds, homepage, and sitemap."""
        cutoff_dt = parse_iso_datetime(modified_after) if modified_after else None
        discovered: Dict[int, Dict[str, Any]] = {}

        # 1. Paginate RSS Feed (/feed/?paged=N)
        page = 1
        limit_pages = max_pages if max_pages and max_pages > 0 else 1000
        while page <= limit_pages:
            try:
                feed_items = self.parse_rss_feed_page(page=page)
            except Exception as e:
                logger.warning(f"[{self.source_key}] Stopping RSS feed pagination at page {page}: {e}")
                break

            if not feed_items:
                break

            any_recent = False
            for item in feed_items:
                tid = item["tune_id"]
                if tid not in discovered:
                    discovered[tid] = item
                item_dt = parse_iso_datetime(item.get("published_at"))
                if cutoff_dt is None or (item_dt and item_dt >= cutoff_dt):
                    any_recent = True

            if page % 50 == 0:
                logger.info(f"[{self.source_key}] Scanned RSS feed page {page} ({len(discovered)} unique tunes discovered so far)...")

            if mode == "incremental" and cutoff_dt is not None and not any_recent:
                logger.info(f"[{self.source_key}] Reached incremental cutoff at RSS page {page}.")
                break

            page += 1

        # 2. Homepage discovery (catches featured/promoted tunes)
        if include_homepage:
            for item in self.discover_homepage_tunes():
                tid = item["tune_id"]
                if tid not in discovered:
                    discovered[tid] = item

        # 3. Sitemap recent tunes discovery (catches modified/newly indexed tunes)
        if include_sitemap_recent and include_sitemap_recent > 0:
            for item in self.discover_sitemap_tunes(limit=include_sitemap_recent):
                tid = item["tune_id"]
                item_dt = parse_iso_datetime(item.get("lastmod"))
                if mode == "incremental" and cutoff_dt is not None and item_dt and item_dt < cutoff_dt:
                    continue
                if tid not in discovered:
                    discovered[tid] = item

        # Sort newest tune_id first
        ordered_entries = sorted(discovered.values(), key=lambda x: x["tune_id"], reverse=True)
        if skip_tune_ids:
            before_count = len(ordered_entries)
            ordered_entries = [e for e in ordered_entries if e["tune_id"] not in skip_tune_ids]
            skipped = before_count - len(ordered_entries)
            if skipped > 0:
                logger.info(f"[{self.source_key}] Skipped {skipped} already-archived tunes.")

        if max_posts and max_posts > 0:
            ordered_entries = ordered_entries[:max_posts]

        logger.info(f"[{self.source_key}] Discovered {len(ordered_entries)} candidate tunes to fetch.")

        worker_count = max(1, int(workers or 1))
        if worker_count <= 1 or len(ordered_entries) <= 1:
            for entry in ordered_entries:
                try:
                    yield self.fetch_tune_detail(entry["url"], rss_meta=entry)
                except Exception as e:
                    logger.error(f"[{self.source_key}] Failed to fetch tune {entry['url']}: {e}")
                    continue
            return

        chunk_size = max(20, worker_count * 8)
        for i in range(0, len(ordered_entries), chunk_size):
            batch = ordered_entries[i : i + chunk_size]
            with ThreadPoolExecutor(max_workers=worker_count) as pool:
                future_map = {
                    pool.submit(self.fetch_tune_detail, entry["url"], entry): entry
                    for entry in batch
                }
                for fut in as_completed(future_map):
                    entry = future_map[fut]
                    try:
                        yield fut.result()
                    except Exception as e:
                        logger.error(f"[{self.source_key}] Failed to fetch tune {entry['url']}: {e}")
