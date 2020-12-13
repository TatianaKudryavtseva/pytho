class Worker:
    def __init__(self, name, surname, position, position_salary):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = position_salary

position_salary = {'wage': '', 'bonus': ''}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total_incom = float(self._incom['wage']) + float(self._incom['bonus'])
        return total_incom

data = Position('Jack', 'Wall', 'manager', {'wage': '400', 'bonus': '75'})
print(data.get_full_name())
print(data.get_total_income())