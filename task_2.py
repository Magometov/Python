import re

import requests


def file_pars(all_lines):
    for line in all_lines:
        first_part = re.compile(r"^(?:[\d*\.*]+)")
        second_part = re.compile(r"(\d{2}/)(\w+/)(\d{4})(?:[:\d+]+)(?:[\s+\d+]*)")
        third_part = re.compile(r"[A-Z]{3}")
        fourth_part = re.compile(r"(/\w{5,})(/\w+)")
        fifth_part = re.compile(r"\d{3}\s")
        some_sixth_object = re.compile(r'\s(?:[0-9]+)\s\"-"')
        some_sixth_part = some_sixth_object.search(line).group()
        sixth_part = some_sixth_part.split(' ')[1]
        result_tuple = (first_part.search(line).group(),
                        second_part.search(line).group(),
                        third_part.search(line).group(),
                        fourth_part.search(line).group(),
                        fifth_part.search(line).group(),
                        sixth_part
                        )

        print(result_tuple)


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(url)
print(file_pars(response.text.strip().split('\n')))
