# টেকটিউনস আর্কাইভ (Techtunes Archive)
### *মেতে উঠুন প্রযুক্তির সুরে — Automated Daily Mirror & Digital Preservation Platform for [techtunes.io](https://www.techtunes.io/)*

[![Daily Techtunes Sync](https://github.com/Royal-Technologies/techtunes/actions/workflows/daily-sync.yml/badge.svg)](https://github.com/Royal-Technologies/techtunes/actions/workflows/daily-sync.yml)
[![Archive Validation & Tests](https://github.com/Royal-Technologies/techtunes/actions/workflows/validate.yml/badge.svg)](https://github.com/Royal-Technologies/techtunes/actions/workflows/validate.yml)
[![Deploy Static Archive to GitHub Pages](https://github.com/Royal-Technologies/techtunes/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Royal-Technologies/techtunes/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.12+](https://img.shields.io/badge/Python-3.12%2B-green.svg)](pyproject.toml)

---

## 1. Overview

**Techtunes Archive (টেকটিউনস আর্কাইভ)** is an automated, zero-server digital preservation and daily mirror platform for **Techtunes** (`https://www.techtunes.io/`), modeled after the `mehdi-writing-archive` architecture and themed with Techtunes' signature Deep Purple palette (`#673ab7`, `#7e57c2`, `#9575cd`).

Every day at **06:00 AM BST (00:00 UTC)** via GitHub Actions, the engine fetches new and updated tunes, tuners (authors), categories, tags, and featured media directly from `https://www.techtunes.io/` and updates:
- **SQLite 3 Database** (`database/archive.sqlite`) with **FTS5** full-text search (`unicode61` tokenizer supporting Bengali & English).
- **UTF-8 Markdown Files** (`articles/techtunes/{bangla|english}/{year}/...md`) with YAML frontmatter.
- **Deterministic JSON Exports** (`exports/articles.json`, `categories.json`, `tags.json`, `authors.json`, `manifest.json`).
- **Static Archive Website** (`website/`) hosted live via GitHub Pages at `https://royal-technologies.github.io/techtunes/`.

---

## 2. Repository Structure

```
techtunes/
├── .github/workflows/          # Automated daily sync, validation, backup & GitHub Pages deploy
├── config/                     # Source URLs, sync settings, media SSRF policy
├── database/                   # SQLite schema, migrations, and archive.sqlite
├── articles/                   # Preserved tunes in Markdown (.md) with YAML frontmatter
├── media/                      # Locally archived featured images (SHA-256 deduplicated)
├── exports/                    # Deterministic JSON exports & manifest
├── scripts/                    # Ingestion, build, validation, backup, and restore CLI
├── tests/                      # Automated pytest suite
└── website/                    # Zero-backend static website (Techtunes Deep Purple theme)
```

---

## 3. Quick Start & CLI Usage

```bash
pip install -r requirements.txt
python scripts/migrations.py
python scripts/sync.py --mode full --max-pages 3
python scripts/build.py
python scripts/validate.py
pytest -v
```

| Command | Description |
| :--- | :--- |
| `python scripts/sync.py --mode incremental` | Daily incremental sync from `techtunes.io` |
| `python scripts/sync.py --mode full --max-pages 10` | Deep backfill across 10 RSS feed pages |
| `python scripts/build.py` | Rebuilds search index, JSON exports, sitemap, and robots.txt |
| `python scripts/validate.py` | Validates SQLite integrity, FTS5, Markdown, and JSON exports |
| `python scripts/report.py` | Generates live archive status & health report |
| `python scripts/backup.py` | Creates a 3-2-1 zip backup with SHA-256 checksum |
| `python scripts/restore.py --rebuild-database` | Rebuilds SQLite database solely from Markdown files |

---

## 4. Live Deployment

- **GitHub Repository**: https://github.com/Royal-Technologies/techtunes
- **GitHub Pages URL**: https://royal-technologies.github.io/techtunes/
- **Content Source**: https://www.techtunes.io/
