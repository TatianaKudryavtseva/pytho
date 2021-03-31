class Warehouse():
    def __init__(self, name):
        self.name = name

class Equipment(Warehouse):
    def __init__(self, name, count):
        self.number_item = name
        self.count = count

    #def total_items(self):
        #items = {'printer': [], 'scanner': [], 'xerox': []}
        #items[self.ls[0]] += 1

class Printer(Equipment):
    def __init__(self, number_item, color_print):
        self.number_item = number_item
        self.color_print = color_print

    def accept(self):
        item = ('printer', self.number_item, self.color_print)
        return item

class Scanner(Equipment):
    def __init__(self, number_item, type_scan):
        self.number_item = number_item
        self.type_scan = type_scan

    def accept(self):
        item = ('scanner', self.number_item, self.type_scan)
        return item

class Xerox(Equipment):
    def __init__(self, number_item, size):
        self.number_item = number_item
        self.size = size

    def accept(self):
        item = ('xerox', self.number_item, self.size)
        return item

first = Printer('7645hgf', 'black_white')
second = Scanner('34qw', 'tablet')
third = Xerox('65yt', 'full size')
print(first.accept())
print(second.accept())
print(third.accept())
