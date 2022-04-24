class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income,
                        'bonus': 15000
                        }


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return f"Доход + премия: {self._income['wage'] + self._income['bonus']} руб."


a = Position('Anzor', 'Magometov', 'Python Developer', 100000)
print(a.get_full_name())
print(a.get_total_income())
