import pprint as pp


def thesaurus_adv(*names):
    result = {}
    for name in names:
        last_name = name.split()[1]
        result[last_name[0]] = {}
    for name in names:
        first_name, last_name = name.split()
        result[last_name[0]].update({first_name[0]: []})
    for name in names:
        first_name, last_name = name.split()
        result[last_name[0]][first_name[0]].append(name)

    return result


pp.pprint(
    thesaurus_adv(
        "Иван Сергеев", "Инна Серова", "Петр Алексеев",
        "Илья Иванов", "Анна Савельева"
    ),
    indent=4
)
