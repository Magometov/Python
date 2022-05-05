class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + i{self.y}'

    def __add__(self, other):
        return f'{self.x + other.x} + i{self.y + other.y}'

    def __mul__(self, other):
        return f'{(self.x * other.x - self.y * other.y)} + {(self.x * other.y + other.x * self.y)}i'


num1 = ComplexNumber(2, 2)
num2 = ComplexNumber(2, 2)
print(num1 * num2)
