class Number_error(Exception):

    @staticmethod
    def is_number():
        num_ls = []
        while True:
            el = input()
            if el != 'stop':
                try:
                    num_ls.append(int(el))
                except:
                    print('Не является числом')
            else:
                break
        return num_ls

print(Number_error.is_number())



