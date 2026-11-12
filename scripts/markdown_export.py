"""Markdown Exporter & Parser for Techtunes Archive.

Converts Techtunes HTML content to clean Markdown, generates YAML frontmatter,
and supports bidirectional parsing to rebuild the database from Markdown.
"""

from __future__ import annotations

import re
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import markdownify
import yaml
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT_DIR / "articles"

# Regex to detect Bengali Unicode characters
BENGALI_CHAR_PATTERN = re.compile(r"[\u0980-\u09FF]")


def detect_language(title: str, text: str, default_language: str = "bn") -> str:
    """Detects whether text is primarily Bengali ('bn') or English ('en')."""
    sample = f"{title} {text[:1000]}"
    bengali_chars = len(BENGALI_CHAR_PATTERN.findall(sample))
    if bengali_chars >= 10:
        return "bn"
    if default_language == "bn" and bengali_chars > 0:
        return "bn"
    if bengali_chars == 0 and len(sample.strip()) > 0:
        return "en"
    return default_language


def sanitize_slug(slug: str) -> str:
    """Normalizes and cleans a slug for cross-platform filesystem safety."""
    if not slug:
        return "untitled"
    slug = urllib.parse.unquote(slug)
    cleaned = re.sub(r'[\'\"`’‘<>:"/\\|?*\x00-\x1f]', "", slug)
    cleaned = re.sub(r"\s+", "-", cleaned).strip("-.")
    return cleaned.lower() if cleaned else "untitled"


def html_to_clean_markdown(html_content: str) -> str:
    """Converts Techtunes HTML into standardized Markdown while preserving structure."""
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, "html.parser")

    # Promote lazy-loaded images (data-src -> src)
    for img in soup.find_all("img"):
        data_src = img.get("data-src") or img.get("data-lazy-src")
        if data_src:
            img["src"] = data_src
        src = img.get("src", "")
        if src.startswith("data:image/svg+xml"):
            img.decompose()

    # Convert iframes to visible archival reference links
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src") or iframe.get("data-src") or ""
        if src:
            iframe.replace_with(f"\n\n[Embedded External Content: {src}]\n\n")
        else:
            iframe.decompose()

    # Strip ad blocks, scripts, styles, and noscript tags
    for selector in [".techtunes-adx", ".adsbygoogle", "ins[data-revive-id]"]:
        for el in soup.select(selector):
            parent = el.parent
            el.decompose()
            if parent and parent.name == "div" and not parent.get_text(strip=True) and not parent.find(["img", "iframe"]):
                parent.decompose()

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    cleaned_html = str(soup)

    md = markdownify.markdownify(
        cleaned_html,
        heading_style=markdownify.ATX,
        bullets="-",
        strip=["script", "style"],
    )

    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def format_yaml_frontmatter(metadata: Dict[str, Any]) -> str:
    """Serializes metadata dict into valid YAML frontmatter."""
    yaml_text = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{yaml_text}---\n\n"


def parse_markdown_file(file_path: Path | str) -> Tuple[Dict[str, Any], str]:
    """Parses a Markdown file into frontmatter metadata and body text."""
    path = Path(file_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_frontmatter = parts[1]
            body = parts[2].lstrip()
            metadata = yaml.safe_load(raw_frontmatter) or {}
            return metadata, body

    return {}, content


def determine_article_path(
    source_key: str,
    language: str,
    published_at: str,
    slug: str,
    wp_post_id: int,
    base_dir: Optional[Path] = None,
) -> Path:
    """Determines the canonical file path: articles/{source}/{language}/{year}/{slug}.md."""
    base = base_dir or ARTICLES_DIR
    lang_folder = "bangla" if language == "bn" else "english"

    year = "unknown"
    if published_at:
        try:
            year = str(datetime.fromisoformat(published_at.replace("Z", "+00:00")).year)
        except Exception:
            match = re.match(r"^(\d{4})", published_at)
            if match:
                year = match.group(1)

    clean_slug = sanitize_slug(slug)

    dir_path = base / source_key / lang_folder / year
    dir_path.mkdir(parents=True, exist_ok=True)

    candidate = dir_path / f"{clean_slug}.md"

    if candidate.exists():
        try:
            meta, _ = parse_markdown_file(candidate)
            existing_wp_id = meta.get("wordpress_id")
            if existing_wp_id and existing_wp_id != wp_post_id:
                candidate = dir_path / f"{clean_slug}-{wp_post_id}.md"
        except Exception:
            candidate = dir_path / f"{clean_slug}-{wp_post_id}.md"

    return candidate


def save_article_markdown(
    file_path: Path,
    metadata: Dict[str, Any],
    markdown_body: str,
) -> None:
    """Atomically writes article metadata and Markdown body to disk in UTF-8."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = format_yaml_frontmatter(metadata)
    full_content = frontmatter + markdown_body + "\n"

    tmp_path = file_path.with_suffix(".tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    tmp_path.replace(file_path)
