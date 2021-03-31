class Division_error(Exception):

    def own_del(self):
        try:
            num1 = int(input('Введите делимое'))
            num2 = int(input('Введите делитель'))
            if num2 == 0:
                raise Division_error('Вы пытаетесь делить на ноль')
        except Division_error as err:
            return err
        else:
            return num1 / num2

for _ in range(3):
    a = Division_error()
    print(a.own_del())