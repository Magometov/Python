class MyDivision(Exception):
    pass


def division(num1, num2):
    if num2 <= 0:
        raise MyDivision('Делить на ноль нельзя!')
    return num1 / num2


division(2, 0)
