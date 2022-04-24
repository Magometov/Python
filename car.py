class Car:
    def __init__(self, color, name, is_police, speed=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed is not None:
            return f"Машина поехала"
        return f'Машина стоит'

    def stop(self):
        if self.speed is None:
            return f'Машина стоит'
        return f'Машина едет'

    def turn(self, direction=None):
        if direction is None:
            return f'Машина едет прямо'
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'{self.speed} км.ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысели допустимую скорость! Допустимый показатель: 60 км.ч"
        return f"{self.speed} км.ч"


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысели допустимую скорость! Допустимый показатель: 40 км.ч"
        return f"{self.speed} км.ч"


class SportCar(Car):
    def __init__(self, color, name, is_police, speed):
        super().__init__(color, name, is_police)
        self.speed = speed

    def show_speed(self):
        if self.speed < 100:
            return f"Что-то ты медленно едешь для такой машины, ускорься!"
        return self.speed


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)

    def police(self):
        if self.is_police:
            return f"Мигалки включены! Работает полиция!"
        return f'У нас все тихо'


a = Car('Black', 'Mers', False, 50)
print(a.show_speed())

town = TownCar('Black', 'Mers', False, 70)
print(town.show_speed())

work = WorkCar('Black', 'Mers', False, 50)
print(work.show_speed())

sport = SportCar('Black', 'Mers', False, 50)
print(sport.show_speed())

police = PoliceCar('White', 'Toyota', True)
print(police.police())

