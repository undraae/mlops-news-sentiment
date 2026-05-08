import pytest
from src.mlops_news_sentiment.data.ingest import fetch_news

def test_fetch_news():
    articles = fetch_news()
    assert len(articles) > 0  # Check that articles were returned
    for article in articles:
        assert all(key in article for key in ['id', 'source', 'title', 'url', 'published_at', 'collected_at'])

def test_saved_csv():
    # Test to be implemented depending on your CSV save functionality
    pass

