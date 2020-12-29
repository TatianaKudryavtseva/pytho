from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    @abstractmethod
    def rate(self):
        pass

    def __add__(self, other):
        return round((self.rate + other.rate), 2)

class Coat(Clothes):

    @property
    def rate(self):
        coat_rate = self.size / 6.5 + 0.5
        return round(coat_rate, 2)

class Costume(Clothes):

    @property
    def rate(self):
        costume_rate = self.height * 2 + 0.3
        return round(costume_rate, 2)

a = Coat(40, 1.78)
b = Costume(46, 1.7)
print(a + b)

