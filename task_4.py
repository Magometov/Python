def unification():
    with open('users.csv', 'r', encoding='utf-8') as first_file:
        with open('hobby.csv', 'r', encoding='utf-8') as second_file:

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


with open('users_hobby.txt', 'a', encoding='utf-8') as result_file:
    for i in unification():
        result_file.write(i + "\n")
