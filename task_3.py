with open('users.csv', 'r', encoding='utf-8') as first_file:
    users = first_file.readlines()

with open('hobby.csv', 'r', encoding='utf-8') as second_file:
    hobbies = second_file.readlines()

result = {}
if len(users) == len(hobbies):
    for user, hobby in zip(users, hobbies):
        result.update({
            user.replace(',', ' ').strip(): hobby.strip()
        })

elif len(users) > len(hobbies):
    for user, hobby in zip(users, hobbies):
        result.update({
            user.replace(',', ' ').strip(): hobby.strip()
        })
    diff = len(users) - len(hobbies)
    while diff > 0:
        last_el = users.pop()
        result.update({
            last_el.replace(',', ' ').strip(): None
        })
        diff -= 1

elif len(users) > len(hobbies):
    print('Выходим из скрипта с кодом 1')


print(result)
