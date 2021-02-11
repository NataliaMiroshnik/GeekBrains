x = float(input('Введите положительное число'))
while x < 0:
    x = float(input('Упс. Введено отрицательное число. Введите еще раз положительно число'))
y = int(input('Введите отрицательно число'))
while y > 0:
    y = int(input('Упс. Введено положительно число. Введите еще раз отрицательно число'))
# def my_func= lambda x, y: x ** y
def my_func(x, y):
    count = 0
    result = 1
    while count != (-y):
        result *= (1/x)
        count +=1
    return result
print(my_func(x, y))
#print(pow(x,y))