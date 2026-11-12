# Contributing to Techtunes Archive

Thank you for helping improve the Techtunes Archive platform!

## Development Setup

```bash
pip install -r requirements.txt
pytest -v
python scripts/validate.py
```

## Guidelines

1. Keep `scripts/techtunes.py` resilient to HTML layout updates and rate limits.
2. Ensure all exported files (`exports/`, `articles/`, `website/data/`) remain UTF-8 encoded.
3. Run `pytest -v` and `python scripts/validate.py` before opening a pull request.
