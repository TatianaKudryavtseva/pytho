class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = ''

    def go(self):
        return 'Машина поехала' if self.speed > 0 else 'Машина остановилась'

    def stop(self):
        return 'Машина остановилась' if self.speed == 0 else 'Машина поехала'

    def turn_direction():
        pass

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'

class PoliceCar(Car):
    def police(self):
        return 'Это полицейская машина'

opel = WorkCar(60, 'silver', 'Opel')
print(opel.go())
print(opel.show_speed())
ford = PoliceCar(80, 'blue', 'Focus')
print(ford.police())