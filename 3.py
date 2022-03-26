def greetings(new_list):
    for words in new_list:
        name = words.split()[-1]
        print(f'Привет, {name[0].upper() + name[1:].lower()}!')


greetings(['инжинер-конструктор Игорь',
           'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй',
           'директор аэлита'
           ])
