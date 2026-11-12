"""Unit tests for backup packaging, integrity verification, and database reconstruction."""

import unittest.mock as mock
from pathlib import Path

from scripts.backup import create_backup_package
from scripts.database import get_db, init_database
from scripts.markdown_export import save_article_markdown
from scripts.restore import rebuild_database_from_markdown, verify_backup


def test_rebuild_database_from_markdown_files(tmp_path: Path):
    """Test that SQLite database can be reconstructed from Techtunes Markdown files."""
    articles_dir = tmp_path / "articles" / "techtunes" / "bangla" / "2026"
    articles_dir.mkdir(parents=True, exist_ok=True)

    meta = {
        "archive_id": "techtunes-1024973",
        "source": "techtunes",
        "wordpress_id": 1024973,
        "title": "ফ্রি AI স্কিল শিখে ক্যারিয়ার গড়ুন",
        "slug": "tips-and-tricks-1024973",
        "language": "bn",
        "published_at": "2026-11-10T13:32:00+00:00",
        "categories": ["টিপস এন্ড ট্রিকস"],
        "tags": ["অনলাইন পড়াশোনা"],
        "original_url": "https://www.techtunes.io/tips-and-tricks/tune-id/1024973",
        "author": "মো আতিকুর ইসলাম",
        "content_hash": "hash1024973",
    }
    body = "টেকটিউনস থেকে সংরক্ষিত বাংলা টিউন।"

    md_file = articles_dir / "tips-and-tricks-1024973.md"
    save_article_markdown(md_file, meta, body)

    target_db = tmp_path / "rebuilt.sqlite"

    with mock.patch("scripts.restore.ROOT_DIR", tmp_path), \
         mock.patch("scripts.restore.get_db_path", return_value=target_db):

        count = rebuild_database_from_markdown(target_db)
        assert count == 1

        with get_db(target_db) as conn:
            post = conn.execute("SELECT * FROM posts WHERE archive_id = 'techtunes-1024973'").fetchone()
            assert post is not None
            assert post["title"] == "ফ্রি AI স্কিল শিখে ক্যারিয়ার গড়ুন"
            assert post["language"] == "bn"


def test_backup_and_verify_package(tmp_path: Path):
    """Test creating a backup package and verifying its checksum and zip integrity."""
    backup_dir = tmp_path / "backups"

    with mock.patch("scripts.backup.ROOT_DIR", tmp_path), \
         mock.patch("scripts.backup.BACKUPS_DIR", backup_dir):

        db_file = tmp_path / "database" / "archive.sqlite"
        init_database(db_file)

        pkg_path = create_backup_package(output_dir=backup_dir)
        assert pkg_path.exists()
        assert pkg_path.suffix == ".zip"
        assert verify_backup(pkg_path) is True
