class Clothes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def fabric_consumption(self):
        if self.name == 'пальто':
            return self.size // 6.5 + 0.5
        elif self.name == 'костюм':
            return 2 * self.size + 0.3
        else:
            raise TypeError('Неизвестное название')


a = Clothes('пальто', 175)
print(a.fabric_consumption())
