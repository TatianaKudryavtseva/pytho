with open('num_sum.txt', 'w') as file:
    file.write('11 12 23 34 45 56 67 78 89')
total = 0
with open('num_sum.txt', 'r') as file:
    for line in file:
        data = [el for el in line.split()]
for i in data:
    total += int(i)
print(f'Сумма чисел = {total}')





