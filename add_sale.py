import sys

with open('bakery.csv', 'a', encoding='utf-8') as file_add:
    file_add.writelines(sys.argv[-1] + '\n')
