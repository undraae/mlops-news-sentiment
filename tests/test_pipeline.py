from unittest.mock import patch
import pandas as pd

from run_pipeline import run_pipeline


@patch("run_pipeline.load_data")
@patch("run_pipeline.analyze_sentiment")
@patch("run_pipeline.transform_news")
@patch("run_pipeline.extract_news")
def test_pipeline_flow(
    mock_extract,
    mock_transform,
    mock_sentiment,
    mock_load
):

    mock_extract.return_value = [{"title": "test"}]

    mock_transform.return_value = pd.DataFrame({
        "text": ["test news"]
    })

    mock_sentiment.return_value = pd.DataFrame({
        "text": ["test news"],
        "sentiment": ["POSITIVE"],
        "confidence": [0.99]
    })

    run_pipeline()

    mock_extract.assert_called_once()
    mock_transform.assert_called_once()
    mock_sentiment.assert_called_once()
    mock_load.assert_called_once()
