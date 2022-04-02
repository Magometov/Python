import requests
import pprint
import json


def currency_rates(val: str):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    val = val.upper()
    dict = json.loads(response.text)
    if not dict['Valute'].get(val):
        return None
    else:
        pprint.pprint(dict['Valute'][val]['Value'])


currency_rates('usd')
