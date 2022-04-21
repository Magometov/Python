import requests
import pprint

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
all_lines = response.text.strip().split("\n")

result = []
for line in all_lines:
    try:
        first_part_line = line.split('- -')[0].strip()
        some_part = line.split('- -')[1].split('] "')[1].split('H')[0]
        second_part_line = some_part.split(' ')[0]
        third_part_line = some_part.split(' ')[1]
        result.append((first_part_line, second_part_line, third_part_line))
    except IndexError:
        pass

pprint.pprint(result, indent=4)
