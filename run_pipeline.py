from src.data.extract import extract_news
from src.data.transform import transform_news
from src.analysis.sentiment import analyze_sentiment
from src.data.load import load_data
import mlflow


def run_pipeline():

    mlflow.set_experiment("news-sentiment")

    mlflow.start_run()

    mlflow.log_param(
    	"model",
    	"distilbert-base-uncased-finetuned-sst-2-english"
    )    

    articles = extract_news()

    df = transform_news(articles)

    df = analyze_sentiment(df)

    mlflow.log_metric("articles_processed", len(df))

    positive_count = len(df[df["sentiment"] == "POSITIVE"])
    negative_count = len(df[df["sentiment"] == "NEGATIVE"])

    mlflow.log_metric("positive_articles", positive_count)
    mlflow.log_metric("negative_articles", negative_count)

    load_data(df)

    mlflow.end_run()


if __name__ == "__main__":
    run_pipeline()
