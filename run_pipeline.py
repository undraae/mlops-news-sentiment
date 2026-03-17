from src.data.extract import extract_news
from src.data.transform import transform_news
from src.analysis.sentiment import analyze_sentiment
from src.data.load import load_data


def run_pipeline():

    articles = extract_news()

    df = transform_news(articles)

    df = analyze_sentiment(df)

    load_data(df)


if __name__ == "__main__":
    run_pipeline()
