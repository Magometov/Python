def thesaurus(*args):
    some_letter = {}
    for i in args:
        some_letter.update({i[0]: []})

    for i in args:
        some_letter[i[0]].append(i)

    return some_letter


print(thesaurus('Олег', 'Игорь', 'Андрей', 'Илья', 'Вероника', 'Виктория', 'Аврора'))
