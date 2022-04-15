user_file = input('Введите название файла с Users: ')
hobbies_file = input('Введит название файла с Hobby: ')
finish_file = input('Введите название конечного файла: ')


def unification_2():
    with open(user_file, 'r', encoding='utf-8') as first_file:
        with open(hobbies_file, 'r', encoding='utf-8') as second_file:
            while True:
                user = first_file.readline()
                hobby = second_file.readline()

                if not user and not hobby:
                    break

                if not hobby:
                    hobby = 'None'

                if not user:
                    user = 'None'

                yield f'{user.strip()}: {hobby.strip()}'


with open(finish_file, 'w', encoding='utf-8') as result_file:
    for i in unification_2():
        result_file.write(i + "\n")
