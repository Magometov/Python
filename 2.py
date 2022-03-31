numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(number):
    if number.istitle():
        number = number.lower()
        print(numbers.get(number).capitalize())
    else:
        print(numbers.get(number))


num_translate_adv('one')
