import requests

from app import config as c
from datetime import datetime

URL = 'http://api.weatherapi.com/v1/forecast.json'


def weather_api() -> list[dict] | None:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date_format = "%Y-%m-%d"

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
        date_obj = datetime.strptime(i['date'], date_format)
        day_of_week = date_obj.weekday()
        day_name = days_of_week[day_of_week]
        day = {
            'day': day_name,
            'date': i['date'][5:],
            'avg_temp': i['day']['avgtemp_c'],
            'wind': i['day']['maxwind_kph'],
            'text': i['day']['condition']['text'],
            'icon': i['day']['condition']['icon']
        }
        forecast.append(day)
    return forecast

