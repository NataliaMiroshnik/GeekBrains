from itertools import count, cycle
start = int(input('Введите начало диапозона'))
stop = int(input('Введите окончание диапозона'))
word = input('Введите элемент для повторения')
n = 0 # счетчик повторов
# my_list = [int(i) for i in range(start, stop + 1)]
# print(*my_list)

for el in count(start):
    if el > stop:
        break
    else:
        print(el)

for el in cycle(word):
    if n > stop:
        break
    print(el)
    n += 1