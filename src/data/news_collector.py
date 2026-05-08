import requests
import pandas as pd
from pathlib import Path

# project root
BASE_DIR = Path(__file__).resolve().parents[2]

# data directory
DATA_DIR = BASE_DIR / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

API_KEY = "19655651163f4c46bd1acefc7855a6d4"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = []

for article in data["articles"]:
    articles.append({
        "title": article["title"],
        "description": article["description"]
    })

# create dataframe
df = pd.DataFrame(articles)

# save dataset
df.to_csv(DATA_DIR / "news.csv", index=False)

print("News data saved:", DATA_DIR / "news.csv")
