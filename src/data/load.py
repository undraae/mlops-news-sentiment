from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_data(df):

    file_path = PROCESSED_DIR / "news_with_sentiment.csv"

    df.to_csv(file_path, index=False)

    print("Processed data saved to:", file_path)
