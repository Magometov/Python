import sys

with open('bakery.csv', 'r', encoding='utf-8') as file_show:
    show = file_show.readlines()
    if sys.argv[-1].isdigit() and not sys.argv[-2].isdigit():
        show_1 = ','.join(show[int(sys.argv[-1]):])
        print(show_1.strip().replace(',', ''))
    if len(sys.argv) > 2:
        num = sys.argv[1:]
        start, finish = int(num[0]), int(num[1])
        show_1 = ','.join(show[start: finish+1])
        print(show_1.strip().replace(',', ''))

    elif not sys.argv[-1].isdigit():
        for i in show:
            print(i.strip())
