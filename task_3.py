class MyDivision(Exception):
    pass


def validate(data):
    if data == 'stop':
        return 'stop'
    if data.isdigit():
        return int(data)
    raise MyDivision


numbers = []
while True:
    data = input('Введите число: ')
    try:
        validate(data)
    except MyDivision:
        print('Вы ввели не число!')
        continue

    if data == 'stop':
        print(numbers)
        break
    else:
        numbers.append(int(data))



