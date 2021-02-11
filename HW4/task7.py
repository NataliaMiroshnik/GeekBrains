from functools import reduce
n = int(input('Введите число n'))

def generator():
    for el in range(1, n+1):
        my_list = [int(i) for i in range(1, el+1)]
        yield reduce(lambda x, y: x*y, my_list)

g = generator()
print(g)

for el in g:
    print(el)