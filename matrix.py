class Matrix:
    def __init__(self, elements_matrix):
        size_0 = len(elements_matrix[0])
        self.elements_matrix = elements_matrix

    @property
    def size_x(self):
        return len(self.elements_matrix[0])

    @property
    def size_y(self):
        return len(self.elements_matrix)

    def __str__(self):
        return "\n".join([''.join(['%d\t' % i for i in row]) for row in self.elements_matrix])

    def __add__(self, other):
        return Matrix(
            [
                [self.elements_matrix[y][x] +
                 other.elements_matrix[y][x] for x in
                 range(self.size_x)]
                for y in range(self.size_y)
            ]
        )


a = Matrix([[1, 2], [3, 4]])
b = Matrix([[1, 2], [3, 4]])
print(a + b)
