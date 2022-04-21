import sys
'''
    Вроде, все работает, но помимо замены элемента по индексу в файле bakery.csv,
    добавляются еще какие-то символы, что с этим делать и откуда они берутся, я не понимаю
    
'''

with open('bakery.csv', 'r+', encoding='utf-8') as edit_file:
    read_line = edit_file.readlines()
    read_line[int(sys.argv[-2]) - 1] = sys.argv[-1] + '\n'

    with open('bakery.csv', 'w', encoding='utf-8') as remove_file:
        edit_file.writelines(read_line)

