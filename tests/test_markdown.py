"""Unit tests for Markdown generation, language detection, and Techtunes HTML cleaning."""

from pathlib import Path
from scripts.markdown_export import (
    detect_language,
    determine_article_path,
    html_to_clean_markdown,
    parse_markdown_file,
    sanitize_slug,
    save_article_markdown,
)


def test_html_to_clean_markdown_techtunes():
    html = """
    <h2>শুরু করার নিয়ম</h2>
    <p>এটি একটি <strong>গুরুত্বপূর্ণ</strong> টিউন।</p>
    <div class="d-flex justify-content-center"><div class="techtunes-adx"><ins data-revive-id="abc"></ins></div></div>
    <p><img class="lazy" data-src="https://dnc.techtunes.io/tDrive/tuner/2026/11/sample.png" src="data:image/svg+xml,%3Csvg%3E%3C/svg%3E" alt="Sample"/></p>
    <script>alert('xss');</script>
    """
    md = html_to_clean_markdown(html)
    assert "## শুরু করার নিয়ম" in md
    assert "**গুরুত্বপূর্ণ**" in md
    assert "https://dnc.techtunes.io/tDrive/tuner/2026/11/sample.png" in md
    assert "data:image/svg+xml" not in md
    assert "alert('xss')" not in md


def test_language_detection():
    assert detect_language("How to Install Docker on Linux", "Step by step instructions", default_language="bn") == "en"
    assert detect_language("বাংলাদেশের প্রযুক্তি খাত", "টেকটিউনস বাংলা ভাষার সবচেয়ে বড় প্রযুক্তি নেটওয়ার্ক") == "bn"


def test_markdown_frontmatter_bidirectional(tmp_path: Path):
    meta = {
        "archive_id": "techtunes-1024973",
        "source": "techtunes",
        "wordpress_id": 1024973,
        "title": "ফ্রি AI স্কিল টিউন",
        "slug": "tips-and-tricks-1024973",
        "language": "bn",
        "published_at": "2026-11-10T13:32:00+00:00",
        "categories": ["টিপস এন্ড ট্রিকস"],
        "content_hash": "abc123hash",
    }
    body = "## সূচনা\n\nটেকটিউনস টিউন।"

    test_file = tmp_path / "test-tune.md"
    save_article_markdown(test_file, meta, body)

    read_meta, read_body = parse_markdown_file(test_file)
    assert read_meta["archive_id"] == "techtunes-1024973"
    assert read_meta["categories"] == ["টিপস এন্ড ট্রিকস"]
    assert "## সূচনা" in read_body


def test_sanitize_slug():
    assert sanitize_slug("Tips & Tricks: 2026?") == "tips-&-tricks-2026"
    assert sanitize_slug("বাংলা স্লাগ টেস্ট") == "বাংলা-স্লাগ-টেস্ট"
    assert sanitize_slug("") == "untitled"


def test_determine_article_path(tmp_path: Path):
    path = determine_article_path(
        source_key="techtunes",
        language="bn",
        published_at="2026-11-10T13:32:00+00:00",
        slug="tips-and-tricks-1024973",
        wp_post_id=1024973,
        base_dir=tmp_path,
    )
    assert "techtunes" in str(path)
    assert "bangla" in str(path)
    assert "2026" in str(path)
    assert path.name == "tips-and-tricks-1024973.md"
