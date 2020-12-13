with open('text_empty.txt', 'a') as file:
    data = True
    while True:
        line = input()
        file.write(line + '\n')
        if line == '':
            data = False
            break
