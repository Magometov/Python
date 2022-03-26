def price_tag(some_list):
    price = []
    for i in some_list:
        rubs, cents = str(i).split('.')
        if int(cents) < 10:
            price.append(rubs + ' руб ' + '0' + cents + ' коп ')
        else:
            price.append(rubs + ' руб ' + cents + ' коп ')
    print(price)


def five_expensive(some_list):
    most_expensive = []
    for i in range(5):
        max_price = max(some_list)
        most_expensive.append(max_price)
        some_list.remove(max_price)
    most_expensive.reverse()
    print(most_expensive)


price_tag(sorted([34.5, 4.4, 55.4]))
price_tag(sorted([34.5, 4.4, 55.4], reverse=True))
five_expensive([34.5, 4.4, 55.4, 56.4, 55.65, 23.55, 98.67])
