a = int(input('Введите числитель'))
b = int(input('Введите знаменатель'))
while b == 0:
    b = int(input('Эй! На ноль делить нельзя! Введите еще раз знаменатель'))
def f(a, b):
    return a / b

print(f(a,b))