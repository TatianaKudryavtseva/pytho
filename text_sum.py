count_line = 0
i = 1
with open('text.txt', 'r') as file:
    for line in file:
        words = [el for el in line.split()]
        print('Количество слов в строке', i, '=', len(words))
        count_line += 1
        i += 1
    print()
print('Количество строк в файле =', count_line)
