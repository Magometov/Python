some = ['в',
        '5',
        'часов',
        '17',
        'минут',
        'температура',
        'воздуха',
        'была',
        '+5',
        'градусов'
        ]
# обособляем числа ковычками
some = some[:1] + ['"', '05', '"'] + some[2:3] + ['"', '17', '"'] + some[4:8] + ['"', '+05', '"'] + some[9:]
print(some)

# формируем строку
str_some = ' '.join(some)
print(str_some)
