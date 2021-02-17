count_line = 0
with open('file2.txt') as file:
    for line in file:
        count_line += 1
        words = line.split()
        print('строка №', count_line, ', количество слов - ', len(words))
print('Общее количество строк в файле - ', count_line)