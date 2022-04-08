tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9A', '7B', '9Б', '9B', '8Б', '10A', '10Б', '9A'
]


def gen_people():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield None, klasses[i]
            i += 1
            j += 1
            break
        else:
            yield tutors[j], klasses[i]
            i += 1
            j += 1


for gen in gen_people():
    print(gen)
