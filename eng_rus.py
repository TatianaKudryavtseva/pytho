data = {'One': 'Один', 'Two': 'Два', 'Three': 'Три','Four': 'Четыре'}
lines = []
with open('english.txt', encoding='utf-8') as file:
    for line in file:
        lines.append(line.split())
with open('russian.txt', 'a') as file_new:
    for el in lines:
        el[0] = data[el[0]]
        file_new.write(' '.join(el) + '\n')
