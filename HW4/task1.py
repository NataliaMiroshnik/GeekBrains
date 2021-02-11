hours = int(input('Введите количество отработанных часов'))
rate = int(input('Введите ставку в час'))
bonus = int(input('Введите премию'))
salary = lambda hours, rate, bonus: hours * rate + bonus
print('Заработная плата сотрудника составляет ', salary(hours, rate, bonus))