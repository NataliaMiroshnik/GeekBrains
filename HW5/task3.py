min_salary = []
total_salary = 0
count = 0
with open('file3.txt') as file:
    data_line = [line.split() for line in file]  # создание вложенных списков из файла
    for str in data_line: # Чтение каждой строки
        str[1] = int(str[1])
        total_salary += str[1]
        count += 1
        if str[1] < 20000:
            min_salary.append(str[0])
        else:
            continue
print('Сотрудники с заработной платой менее 20 тыс.руб.:', *min_salary)
print('Средняя заработная плата всех сотрудников составляет: ', round(total_salary/count, 1))