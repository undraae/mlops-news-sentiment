import pandas as pd
from src.analysis.sentiment import analyze_sentiment

def test_sentiment_columns_created():
    df = pd.DataFrame({
        "text": ["The stock market is doing great today."]
    })

    result = analyze_sentiment(df)

    assert "sentiment" in result.columns
    assert "confidence" in result.columns

def test_sentiment_not_empty():
    df = pd.DataFrame({
        "text": ["This is a test sentence."]
    })

    result = analyze_sentiment(df)

    assert result["sentiment"].iloc[0] is not None
    assert result["confidence"].iloc[0] > 0
