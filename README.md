# mlops-news-sentiment

This project is an end-to-end pipeline for news sentiment analysis.

## Project Structure

- `src/mlops_news_sentiment/`: Main source code.
- `tests/`: Unit and integration tests.
- `data/`: Data storage (raw and processed).
- `models/`: Saved models.
- `mlruns/`: MLflow tracking data.

## Installation

1. Install dependencies:
   ```bash
   make install

## Workflow

1. Collect news data
2. Store raw data
3. Perform sentiment analysis using Hugging Face Transformers
4. Save processed results to data/processed

## Output

The pipeline generates a sentiment analysis dataset containing:
- News title
- Sentiment label
- Confidence score

