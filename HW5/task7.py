import json
profit = {}
with open ('file7.json', 'w') as write:
    with open('file7.txt') as file:
        for line in file:
            el = line.split()
            profit[el[0]] = int(el[2]) - int(el[3])
        average_profit = round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                               len([int(i) for i in profit.values() if int(i) > 0]))
        for_print = [profit , {'Средняя прибыль': average_profit}]
        print('Прибыль фирм: ' f"{profit}", '\n', 'Средняя прибыль прибыльных фирм: ', average_profit)

    json.dump(for_print, write, ensure_ascii=False, indent=4)

