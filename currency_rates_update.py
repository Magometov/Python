import requests
import pprint
import json
import datetime as dt


def currency_rates(val: str):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    try:
        val = val.upper()
        dict = json.loads(response.text)
        pprint.pprint(f"Курс валюты: {dict['Valute'][val]['Value']}", indent=4)
        pprint.pprint(f"Московское время: {start.strftime('%H:%M')}", indent=4)


    except:
        pprint.pprint(f"Ввалюты- {val} не существует!")


if __name__ == '__main__':
    currency_rates('usd')
