class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if (self.cells - other.cells) < 0:
            raise ValueError('разность кол-ва ячеек меньше нуля')
        return self.cells - other.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        return self.cells // other.cells

    def make_order(self, cells_in_row):
        row = self.cells // cells_in_row
        if self.cells % cells_in_row == 0:
            for i in range(row):
                if i + 1 == row:
                    print(f"{'*' * cells_in_row}", end='')
                else:
                    print(f"{'*' * cells_in_row}\\n", end='')
        else:
            if row == 1:
                print(f"{'*' * cells_in_row}\\n", end='')
                print(f"{'*' * (self.cells - cells_in_row)}", end='')
                print('row == 1')
            else:
                print('else')
                for i in range(row):
                    if i + 1 == row:
                        print(f"{'*' * cells_in_row}\\n", end='')
                        print(f"{'*' * (self.cells % cells_in_row)}", end='')
                    else:
                        print(f"{'*' * cells_in_row}\\n", end='')


a = Cell(15)
b = Cell(2)
a.make_order(5)
