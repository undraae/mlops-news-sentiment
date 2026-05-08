.PHONY: install test lint

PYTHON=python3  # Ensure this is set
SRC=src

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	ruff check src/

# ── Pipeline Commands ────────────────────────────────────────
ingest:
	@PYTHONPATH=$(SRC) $(PYTHON) -m mlops_news_sentiment.data.ingest

