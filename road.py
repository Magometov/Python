class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def asphalt_construction(self):
        """
        Примерный расход асфальта на 1 кв.м при толщине слоя 1 см, равен 25 кг
        """
        mass_of_asphalt = self._lenght * self._width * 25 * 5
        return f"Масса асфальта равна: {mass_of_asphalt//1000} т."


a = Road(20, 5000)
print(a.asphalt_construction())
