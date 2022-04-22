# Приношу свои извинения за подобное название переменных

numbers = []
# создаем список из кубов нечетных чисел от 1 до 1000 и выводим на экран
for i in range(1, 1001):
    if i % 2 != 0:
        numbers.append(i ** 3)
print(numbers)


def find():
    # Создаем новый список и записываем туда числа, сумма цифр которыз делится на 7 без остатка
    result = []
    for number in numbers:
        # В переменную suma будем записывать сумму цифр числа, затем проверять делится ли оно на 7 без остатка
        suma = 0
        n = number
        while n > 0:
            digit = n % 10
            suma = suma + digit
            n = n // 10
        if suma % 7 == 0:
            result.append(number)
    print(result)
    # Цикл, который будет считать сумму чисел в нашем списке result
    n = 0
    for res in result:
        n += res

    print(n)


find()
# Цикл, который добавляет 17 к элементам нашего списка numbers не создавая новый список
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 17
print(numbers)
find()
