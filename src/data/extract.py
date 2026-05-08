import requests

API_KEY = "19655651163f4c46bd1acefc7855a6d4"

def extract_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["articles"]
