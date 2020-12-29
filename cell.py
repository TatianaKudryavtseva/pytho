class Cell:
    def __init__(self, cell, nucleus):
        self.cell = int(cell)
        self.nucleus = int(nucleus)

    def __add__(self, other):
        return self.cell * self.nucleus + other.cell * other.nucleus

    def __sub__(self, other):
        return self.nucleus - other.nucleus if (self.nucleus - other.nucleus) > 0 else print('разность меньше 0')

    def __mul__(self, other):
        return self.cell * self.nucleus * other.cell * other.nucleus

    def __truediv__(self, other):
        return (self.cell * self.nucleus) // (other.cell * other.nucleus)

    def make_order(self, count):
        if self.nucleus % count != 0:
            return ('/n'.join(['*' * count for _ in range(self.nucleus // count)]) + '/n' + '*' * (self.nucleus % count))
        else:
            return ('/n'.join(['*' * count for _ in range(self.nucleus // count)]))

x = Cell(1, 8)
y = Cell(1, 6)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
z = Cell(1, 12)
print(z.make_order(5))
h = Cell(1, 15)
print(h.make_order(5))
