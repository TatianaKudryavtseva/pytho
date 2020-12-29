class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            return 'Горит красный свет. Ждите 7 секунд'
            self.__color = 'yellow'
            return 'Внимание, через 2 секунды загорится зеленый'
        elif self.__color == 'yellow':
            return 'Внимание, через 2 секунды загорится зеленый'
            self.__color = 'green'
            return 'Можете ехать'
        elif self.__color == 'green':
            return 'Можете ехать. Через 15 секунд загорится красный'
            self.__color = 'red'
            return 'Загорелся красный свет. Стойте'

run = TrafficLight('green')
print(run.running())
run = TrafficLight('red')
print(run.running())
un = TrafficLight('yellow')
print(run.running())




