import os
import feedparser
import pandas as pd
from datetime import datetime
from mlops_news_sentiment.config import RAW_NEWS_CSV, RSS_FEEDS
from loguru import logger

def fetch_news():
    """
    Fetch news articles from predefined RSS feeds.
    """
    articles = []
    
    for feed_url in RSS_FEEDS:
        logger.info(f"Fetching feed: {feed_url}")
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries:
            article = {
                "id": entry.link.split("/")[-1],  # Use link as ID
                "source": entry.source.title if "source" in entry else feed.feed.title,
                "title": entry.title,
                "description": entry.get("description", ""),
                "url": entry.link,
                "published_at": entry.published,
                "collected_at": datetime.utcnow().isoformat(),
            }
            articles.append(article)
    
    return articles

def save_to_csv(articles):
    """
    Save the list of articles to a CSV file.
    """
    logger.info(f"Saving {len(articles)} articles to {RAW_NEWS_CSV}")
    df = pd.DataFrame(articles)
    df.drop_duplicates(subset=["url"], inplace=True)  # Ensure unique articles
    df.to_csv(RAW_NEWS_CSV, index=False)

def main():
    articles = fetch_news()
    save_to_csv(articles)

if __name__ == "__main__":
    logger.add("data_ingestion.log", rotation="1 MB")  # Log file
    main()

