import requests

from app import config as c
from datetime import datetime

URL = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={c.news_api_key}'


def news_api() -> list[dict] | None:
    response = requests.get(url=URL)
    data = response.json()['articles'][0:3]
    for i in data:
        data['publishedAt'] = data['publishedAt'][:10]
    return data

