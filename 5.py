import random


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    some_list = []
    while number > 0:
        some_str = random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives)
        some_list.append(some_str)
        number -= 1

    return some_list


print(get_jokes(2))
