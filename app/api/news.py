import requests

from app import config as c

URL = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={c.news_api_key}'


def news_api() -> list[dict] | None:
    response = requests.get(url=URL)
    data = response.json()['articles']
    for i in data:
        i['publishedAt'] = i['publishedAt'][:10]
    return data

