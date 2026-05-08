import pandas as pd

def transform_news(articles):

    records = []

    for article in articles:
        records.append({
            "title": article["title"],
            "description": article["description"]
        })

    df = pd.DataFrame(records)

    df["text"] = df["title"] + " " + df["description"]

    df = df.dropna()

    return df
