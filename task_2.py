import requests
import pprint

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
all_lines = response.text.strip().split("\n")

all_ip_address = []
for line in all_lines:
    all_ip_address.append(line.split('- -')[0].strip())

common = 0
for el in all_ip_address:
    if all_ip_address.count(el) > common:
        spam = el
        common = all_ip_address.count(el)

print(f'Спамер - это {spam}, количество: {common}')