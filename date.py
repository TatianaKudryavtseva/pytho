class Date():

    @classmethod
    def get_number(cls, date):
        return [int(num) for num in date.split('-')]

    @staticmethod
    def valid(date):
        num_list = Date.get_number(date)
        print('True' if 1 <= num_list[0] <= 31 and 1 <= num_list[1] <= 12 and 1990 <= num_list[2] <= 2020 else 'False')

a = Date.get_number('13-06-1990')
print(a)
Date.valid('32-08-2000')
Date.valid('13-06-1990')

