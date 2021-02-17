from random import randint
with open('file5.txt', 'w+') as file:
    file.write(' '.join([str(randint(1, 100)) for i in range(20)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))