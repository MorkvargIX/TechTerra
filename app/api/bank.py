import requests

import calendar
from datetime import datetime, timedelta


def bank_api() -> dict | None:
    data: dict = {}
    current_date = datetime.now()
    last_12_months_dates = []
    for i in range(1, 13):
        prev_month_date = current_date - timedelta(days=current_date.day)
        last_12_months_dates.append(prev_month_date.strftime("%Y%m%d"))
        current_date = prev_month_date
    last_12_months_dates.reverse()
    for month in last_12_months_dates:
        response = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={month}&json')
        date_obj = datetime.strptime(month, "%Y%m%d")
        month_name = date_obj.strftime("%B")
        data[month_name] = response.json()[24]['rate']
    print(data)
    return data
