class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Будем рисовать ручкой"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Будем рисовать карандашом"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Будем рисовать маркером"


a = Stationary('House')
print(a.draw())

pen = Pen('House')
print(pen.draw())

pencil = Pencil('House')
print(pencil.draw())

handle = Handle('House')
print(handle.draw())
