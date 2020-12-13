import json
with open('firm.txt', 'r', encoding='utf-8') as file:
    count = 0
    total_profit = 0
    dict_profit = {}
    for line in file:
        content = line.split()
        name, profit = content[0], float(float(content[2]) - float(content[3]))
        dict_profit[name] = profit
        count += 1
        if profit < 0:
            continue
        else:
           total_profit += profit
data = [dict_profit, {'average_profit': round(total_profit / count, 2)}]
with open('profit.json', 'w') as file_json:
    json.dump(data, file_json)


