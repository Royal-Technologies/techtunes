"""Unit tests for Techtunes HTML parsing and synchronization engine."""

from pathlib import Path
from unittest.mock import patch

from scripts.database import get_db, init_database
from scripts.sync import ArchiveSynchronizer
from scripts.techtunes import TechtunesClient


SAMPLE_TUNE_HTML = """<!DOCTYPE html>
<html lang="bn-BD">
<head>
  <meta property="og:title" content="ফ্রি AI স্কিল গাইড | Techtunes | টেকটিউনস">
  <meta property="article:published_time" content="2026-11-10T13:32+00:00">
  <meta property="article:modified_time" content="2026-11-10T13:32+00:00">
  <meta property="og:image" content="https://dnc.techtunes.io/tDrive/tuner/2026/11/hero.png">
</head>
<body>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg mb-5">
        <img class="lazy" data-src="https://dnc.techtunes.io/tDrive/tuner/2026/11/hero-640x360.png" src="data:image/svg+xml,%3Csvg%3E%3C/svg%3E">
      </div>
      <div class="col-lg">
        <div class="flex-center">
          <h2 class="h2-responsive text-white">\ufeffফ্রি AI স্কিল গাইড</h2>
        </div>
      </div>
    </div>
  </div>
  <div class="card z-depth-1 casecade-up">
    <div class="card-body pt-0">
      <div>টিউন বিভাগ <span class="mdb badge"><a href="https://www.techtunes.io/category/tips-and-tricks">টিপস এন্ড ট্রিকস</a></span></div>
    </div>
    <div class="card-body px-3 px-sm-4 mb-3">
      <p>টেকটিউনস বাংলা প্রযুক্তি টিউন বিস্তারিত।</p>
      <div class="techtunes-adx"><ins data-revive-id="123"></ins></div>
      <p><img class="lazy" data-src="https://dnc.techtunes.io/tDrive/tuner/2026/11/step1.png" src="data:image/svg+xml,%3Csvg%3E%3C/svg%3E"></p>
    </div>
  </div>
  <div class="pt-4 pt-md-7 pb-10">
    <img class="avatar lazy" data-src="https://dnc.techtunes.io/tDrive/tuner/avatars/103/avatar.png" src="data:image/svg+xml,%3Csvg%3E%3C/svg%3E">
    <a href="https://www.techtunes.io/tuner/atikurofficial" rel="author">মো আতিকুর ইসলাম</a>
  </div>
</body>
</html>
"""


def test_techtunes_html_parser():
    client = TechtunesClient()
    parsed = client.parse_tune_html(
        "https://www.techtunes.io/tips-and-tricks/tune-id/1024973",
        SAMPLE_TUNE_HTML,
        rss_meta={"rss_terms": ["টিপস এন্ড ট্রিকস", "অনলাইন পড়াশোনা"]},
    )
    assert parsed["id"] == 1024973
    assert parsed["title"] == "ফ্রি AI স্কিল গাইড"
    assert parsed["author"]["name"] == "মো আতিকুর ইসলাম"
    assert parsed["author"]["slug"] == "atikurofficial"
    assert parsed["categories"][0]["name"] == "টিপস এন্ড ট্রিকস"
    assert any(t["name"] == "অনলাইন পড়াশোনা" for t in parsed["tags"])
    assert "https://dnc.techtunes.io/tDrive/tuner/2026/11/step1.png" in parsed["content_html"]
    assert "techtunes-adx" not in parsed["content_html"]


def test_mocked_sync_and_revision_generation(tmp_path: Path):
    db_file = tmp_path / "test_sync.sqlite"
    articles_dir = tmp_path / "articles"
    exports_dir = tmp_path / "exports"

    client = TechtunesClient()
    tune_v1 = client.parse_tune_html(
        "https://www.techtunes.io/tips-and-tricks/tune-id/1024973",
        SAMPLE_TUNE_HTML,
        rss_meta={"rss_terms": ["টিপস এন্ড ট্রিকস", "অনলাইন পড়াশোনা"]},
    )
    tune_v1["featured_image_url"] = None

    tune_v2 = dict(tune_v1)
    tune_v2["title"] = "আপডেটেড ফ্রি AI স্কিল গাইড"
    tune_v2["modified_at"] = "2026-11-11T10:00:00+00:00"

    with patch("scripts.database.get_db_path", return_value=db_file), \
         patch("scripts.sync.ROOT_DIR", tmp_path), \
         patch("scripts.markdown_export.ARTICLES_DIR", articles_dir), \
         patch("scripts.json_export.EXPORTS_DIR", exports_dir):

        init_database(db_file)
        syncer = ArchiveSynchronizer(mode="full")

        source_conf = {
            "key": "techtunes",
            "name": "টেকটিউনস (Techtunes)",
            "domain": "www.techtunes.io",
            "base_url": "https://www.techtunes.io",
            "api_url": "https://www.techtunes.io/feed/",
            "default_language": "bn",
        }

        with patch("scripts.sync.TechtunesClient.get_categories", return_value=[{"id": 1, "name": "টিপস এন্ড ট্রিকস", "slug": "tips-and-tricks"}]), \
             patch("scripts.sync.TechtunesClient.iterate_tunes", return_value=iter([tune_v1])):
            stats = syncer.sync_single_source(source_conf)
            assert stats["posts_created"] == 1
            assert stats["posts_updated"] == 0

        with get_db(db_file) as conn:
            assert conn.execute("SELECT count(*) as c FROM posts").fetchone()["c"] == 1

        syncer.mode = "incremental"
        with patch("scripts.sync.TechtunesClient.get_categories", return_value=[]), \
             patch("scripts.sync.TechtunesClient.iterate_tunes", return_value=iter([tune_v2])):
            stats_inc = syncer.sync_single_source(source_conf)
            assert stats_inc["posts_updated"] == 1
            assert stats_inc["posts_created"] == 0

        with get_db(db_file) as conn:
            assert conn.execute("SELECT count(*) as c FROM post_revisions").fetchone()["c"] == 1
            row = conn.execute("SELECT title FROM posts WHERE archive_id = 'techtunes-1024973'").fetchone()
            assert row["title"] == "আপডেটেড ফ্রি AI স্কিল গাইড"
