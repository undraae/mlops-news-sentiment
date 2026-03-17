from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(df):

    texts = df["text"].tolist()

    results = classifier(texts, batch_size=8)

    df["sentiment"] = [r["label"] for r in results]
    df["confidence"] = [r["score"] for r in results]

    return df
