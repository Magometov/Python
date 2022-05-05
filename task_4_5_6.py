class WarehouseDescription:
    def __init__(self, printer: int, scanner: int, xerox: int):
        self.printer = printer
        self.scanner = scanner
        self.xerox = xerox

    def __str__(self):
        return f"Добро пожаловать на склад техники!\n" \
               f"У нас есть:\n" \
               f"Принторы - {self.printer} шт.\n" \
               f"Сканнеры - {self.scanner} шт.\n" \
               f"Ксероксы - {self.xerox} шт."

    def acceptance(self):
        print('Мы готовы к приемке!')
        printers = int(input('Кол-во принимаемых принтеров: '))
        scanners = int(input('Кол-во принимаемых сканнеров: '))
        xeroxs = int(input('Кол-во принимаемых ксероксов: '))
        self.printer += printers
        self.scanner += scanners
        self.xerox += xeroxs
        return f'По итогу на склад прибыло:\n' \
               f'Принтеров - {printers}\n' \
               f'Сканнеров - {scanners}\n' \
               f'Ксероксов - {xeroxs}'

    def sending(self):
        print('Мы готовы к отправке!')
        printers = int(input('Кол-во отправляемых принтеров: '))
        scanners = int(input('Кол-во отправляемых сканнеров: '))
        xeroxs = int(input('Кол-во отправляемых ксероксов: '))
        self.printer -= printers
        self.scanner -= scanners
        self.xerox -= xeroxs
        return f'По итогу из склада отправлено:\n' \
               f'Принтеров - {printers}\n' \
               f'Сканнеров - {scanners}\n' \
               f'Ксероксов - {xeroxs}'


class Technics:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year


class Printer(Technics):
    def __init__(self, name, country, year, color):
        super().__init__(name, country, year)
        self.color = color


class Scanner(Technics):
    def __init__(self, name, country, year):
        super().__init__(name, country, year)


class Xerox(Technics):
    def __init__(self, name, country, year, color):
        super().__init__(name, country, year)
        self.color = color


b = WarehouseDescription(2, 4, 5)
print(b)
print(b.acceptance())
print('---'*5)
print(b)
print('---'*5)
print(b.sending())
print('---'*5)
print(b)
