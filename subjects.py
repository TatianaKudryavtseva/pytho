my_dict = {}
with open('subjects.txt', encoding='utf-8') as file:
    for line in file:
        name, lessons = line.split(':')
        lessons = lessons.strip()
        total = 0
        for el in lessons.split():
            if el != '—':
                num = (''.join([i for i in el if i in '1234567890']))
                total += int(num)
        my_dict[name] = total
print(my_dict)


