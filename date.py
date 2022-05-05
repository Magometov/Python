import datetime


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def type_int(cls, date):
        my_date = []
        for i in date.split('-'):
            my_date.append(int(i))
        return my_date

    @staticmethod
    def validation_date(day, month, year):
        now_year = datetime.datetime.now()
        if (1 <= day <= 31) and (1 <= month <= 12) and (year <= now_year.year):
            return 'Данные введены верно!'
        raise TypeError('Дата введена не корректно')


a = Date('28-03-2002')
print(Date.type_int('28-03-2002'))
print(a.validation_date(28, 3, 2002))
