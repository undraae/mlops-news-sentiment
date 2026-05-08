# src/mlops_news_sentiment/config.py

# Path to save the raw news data
RAW_NEWS_CSV = 'data/raw_news.csv'

# List of RSS feed URLs to fetch news from
RSS_FEEDS = [
    'https://rss.nytimes.com/services/xml/nyt/HomePage.xml',  # Example 1
    'https://feeds.bbci.co.uk/news/rss.xml',                   # Example 2
    # Add more RSS feed URLs as needed
]

# Optional: Other configurations
# Define constants for scraping parameters, output directories, etc.
TIMEOUT = 10  # Timeout for HTTP requests in seconds

