# mlops-news-sentiment

End-to-end MLOps project for automated news sentiment analysis using Hugging Face Transformers. The pipeline collects news articles, performs sentiment analysis, and stores processed results for further analysis and monitoring.

## Project Structure

- `src/mlops_news_sentiment/` : Main source code
- `tests/` : Unit and integration tests
- `data/` : Raw and processed datasets
- `models/` : Saved models and artifacts
- `mlruns/` : MLflow experiment tracking data
- `.github/workflows/` : GitHub Actions CI pipeline

## Tech Stack

- Python
- Pandas
- Hugging Face Transformers
- Pytest
- GitHub Actions
- MLflow

## Workflow

1. Collect news data
2. Store raw news dataset
3. Transform and preprocess articles
4. Perform sentiment analysis using Hugging Face Transformers
5. Store processed results
6. Track experiments with MLflow
7. Validate changes through GitHub Actions CI

## Output

The pipeline generates a sentiment analysis dataset containing:

- News title
- Article text
- Sentiment label (POSITIVE / NEGATIVE)
- Confidence score

## CI/CD

GitHub Actions automatically executes tests on every push to ensure code quality and pipeline stability.

## MLflow experiment tracking

MLflow is used to track pipeline execution metrics and experiment runs.

Tracked metrics:

- articles_processed
- positive_articles
- negative_articles

Tracked parameters:

- sentiment model name

## Testing

Run tests locally:

 - pytest

GitHub Actions automatically executes tests on every push to ensure code quality and pipeline stability.
 
## Future Improvements

- MLflow experiment tracking
- FastAPI inference service
- Airflow workflow orchestration
- SageMaker-based model training
- Monitoring and alerting
