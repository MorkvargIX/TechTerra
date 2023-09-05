import requests
import config as c

URL = 'http://api.weatherapi.com/v1/forecast.json'


def weather_api() -> list[dict] | None:
    forecast: list = []
    params = {
        'key': c.weather_api_key,
        'q': 'Kiev',
        'days': 7,
        'aqi': 'no',
        'alerts': 'no'
    }
    response = requests.get(url=URL, params=params)
    data = response.json()['forecast']['forecastday']
    for i in data:
        day = {
            'avg_temp': i['day']['avgtemp_c'],
            'wind': i['day']['maxwind_kph'],
            'text': i['day']['condition']['text'],
        }
        forecast.append(day)
    return forecast

