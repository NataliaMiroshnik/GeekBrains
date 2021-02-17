with open('file1.txt', 'w') as write_text:
    while True:
        lines = input('Введите текст')
        write_text.write(lines + '\n')
        if lines == '':
            break