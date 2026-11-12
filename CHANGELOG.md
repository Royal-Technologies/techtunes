# Changelog

## [1.0.0] - 2026-11-12
### Added
- Full Techtunes (`https://www.techtunes.io/`) ingestion engine via RSS feeds, homepage discovery, sitemap updates, and HTML parser (`scripts/techtunes.py`).
- SQLite 3 relational database with FTS5 (`unicode61`) Bengali & English full-text search, revision tracking, and Markdown/JSON tri-layer persistence.
- Techtunes Deep Purple (`#673ab7`, `#7e57c2`, `#9575cd`) static website (`website/`) with dark/light themes, category browser, tag cloud, tuner directory, timeline, and client-side search.
- Automated GitHub Actions workflows for daily sync (`daily-sync.yml`), GitHub Pages deployment (`deploy-pages.yml`), validation (`validate.yml`), and weekly backups (`backup.yml`).
