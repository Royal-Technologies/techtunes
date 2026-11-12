"""Unit tests for SQLite database engine and FTS5 search."""

import sqlite3
from pathlib import Path

import pytest
from scripts.database import get_db, init_database, utc_now_iso
from scripts.migrations import run_migrations


@pytest.fixture
def temp_db(tmp_path: Path):
    """Provides a temporary test database path initialized with schema."""
    db_file = tmp_path / "test_archive.sqlite"
    init_database(db_file)
    return db_file


def test_database_initialization(temp_db: Path):
    """Test that all required archive tables and virtual tables are created."""
    with get_db(temp_db) as conn:
        tables = [
            r["name"] for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        ]

        required_tables = [
            "sites", "authors", "posts", "categories", "tags",
            "post_categories", "post_tags", "media", "post_media",
            "post_revisions", "sync_state", "sync_logs",
            "schema_migrations", "posts_fts"
        ]

        for req in required_tables:
            assert req in tables, f"Missing required table: {req}"


def test_foreign_key_constraints(temp_db: Path):
    """Test that foreign key violations are rejected."""
    with get_db(temp_db) as conn:
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO posts (
                    archive_id, site_id, wp_post_id, title, slug, language,
                    content_html, content_markdown, excerpt, status, post_type,
                    original_url, published_at, modified_at, content_hash,
                    markdown_path, archived_at, created_at, updated_at
                ) VALUES (
                    'fake-999', 999999, 1, 'Fake', 'fake', 'bn',
                    '', '', '', 'publish', 'post',
                    'https://www.techtunes.io/fake', '2026-01-01', '2026-01-01', 'hash',
                    'articles/fake.md', '2026-01-01', '2026-01-01', '2026-01-01'
                )
                """
            )


def test_unique_constraint_post_deduplication(temp_db: Path):
    """Test that (site_id, wp_post_id) duplicate insertions are prevented."""
    now = utc_now_iso()
    with get_db(temp_db) as conn:
        site_id = conn.execute("SELECT id FROM sites LIMIT 1").fetchone()["id"]

        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'techtunes-100', ?, 100, 'Tune 1', 'tune-1', 'bn',
                '', '', '', 'publish', 'post',
                'https://www.techtunes.io/tips/tune-id/100', ?, ?, 'hash1',
                'articles/tune-1.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now),
        )

        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO posts (
                    archive_id, site_id, wp_post_id, title, slug, language,
                    content_html, content_markdown, excerpt, status, post_type,
                    original_url, published_at, modified_at, content_hash,
                    markdown_path, archived_at, created_at, updated_at
                ) VALUES (
                    'techtunes-100-dup', ?, 100, 'Tune 2', 'tune-2', 'bn',
                    '', '', '', 'publish', 'post',
                    'https://www.techtunes.io/tips/tune-id/100', ?, ?, 'hash2',
                    'articles/tune-2.md', ?, ?, ?
                )
                """,
                (site_id, now, now, now, now, now),
            )


def test_fts5_bengali_and_english_search(temp_db: Path):
    """Test FTS5 search with both Bengali and English keywords."""
    now = utc_now_iso()
    with get_db(temp_db) as conn:
        site_id = conn.execute("SELECT id FROM sites LIMIT 1").fetchone()["id"]

        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'techtunes-101', ?, 101, 'Prompt Engineering Guide', 'prompt-101', 'en',
                '<p>Learn AI workflows.</p>',
                'Learn AI workflows and ChatGPT techniques.',
                'AI guide.', 'publish', 'post',
                'https://www.techtunes.io/ai/tune-id/101', ?, ?, 'hash_en',
                'articles/prompt.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now),
        )

        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'techtunes-201', ?, 201, 'টেকটিউনস প্রযুক্তির সুরে নতুন টিউন', 'bangla-201', 'bn',
                '<p>কৃত্রিম বুদ্ধিমত্তা ও অটোমেশন গাইড।</p>',
                'কৃত্রিম বুদ্ধিমত্তা ও অটোমেশন গাইড।',
                'প্রযুক্তি টিউন।', 'publish', 'post',
                'https://www.techtunes.io/ai/tune-id/201', ?, ?, 'hash_bn',
                'articles/bangla.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now),
        )

        en_matches = conn.execute(
            "SELECT archive_id FROM posts_fts WHERE posts_fts MATCH 'Prompt'"
        ).fetchall()
        assert len(en_matches) == 1
        assert en_matches[0]["archive_id"] == "techtunes-101"

        bn_matches = conn.execute(
            "SELECT archive_id FROM posts_fts WHERE posts_fts MATCH 'অটোমেশন'"
        ).fetchall()
        assert len(bn_matches) == 1
        assert bn_matches[0]["archive_id"] == "techtunes-201"


def test_migrations_runner(tmp_path: Path):
    """Test that migrations can be run idempotently."""
    db_file = tmp_path / "migration_test.sqlite"
    count1 = run_migrations(db_file)
    assert count1 >= 0
    count2 = run_migrations(db_file)
    assert count2 == 0
