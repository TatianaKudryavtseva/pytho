data = []
total = 0
salary_min = []
with open('salary.txt', encoding='utf-8') as file:
    for line in file:
        data.append(line.split())
for el in data:
    total += int(el[1])
    if int(el[1]) < 20000:
        salary_min.append(el[0])
print('Фамилии сотрудников с окладом меньше 20 тыс:', *salary_min)
print(f'Средняя величина дохода = {total / len(data)}')