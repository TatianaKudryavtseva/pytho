class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_total(self):
        mass_total = self._length * self._width * mass * thick
        return mass_total

mass = 25
thick = 5
proportions = Road(20, 5000)
print(proportions.mass_total())