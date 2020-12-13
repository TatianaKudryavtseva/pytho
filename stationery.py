class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

one = Stationery('Кисть')
one.draw()
two = Pen('pen')
two.draw()
three = Pencil('pencil')
three.draw()
four = Handle('handler')
four.draw()