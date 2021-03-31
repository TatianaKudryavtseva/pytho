class Complex:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        ls = []
        ls.append(str(int(self.num[0]) + (int(other.num[0]))))
        ls.append('+')
        ls.append(str(int(self.num[2]) + (int(other.num[2]))))
        ls.append('j')
        return ''.join(ls)

    def __mul__(self, other):
        ls = []
        ls.append(str(int(self.num[0]) * (int(other.num[0])) - int(self.num[2]) * (int(other.num[2]))))
        ls.append('+')
        ls.append(str(int(self.num[2]) * (int(other.num[0])) + int(self.num[0]) * (int(other.num[2]))))
        ls.append('j')
        return ''.join(ls)

a = Complex('1+2j')
b = Complex('3+4j')
print(a + b)

x = Complex('4+6j')
y = Complex('3+7j')
print(x * y)