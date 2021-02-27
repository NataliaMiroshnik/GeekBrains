a = int(input('Введите числитель'))
b = int(input('Введите делитель'))
try:
    print(a/b)
except ZeroDivisionError:
    print('Делить на ноль нельзя')
