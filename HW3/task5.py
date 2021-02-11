numbers = (input('Введите числа').upper().split())
stop_word = 'Q'
result = 0
while True:
    if stop_word in numbers:
        stop = numbers.index('Q')
        numbers = numbers[:stop]
        numbers = (float(i) for i in numbers)
        result += sum(numbers)
        print('Сумма введенных значений', result)
        break
    else:
        numbers = (float(i) for i in numbers)
        result = sum(numbers)
        print('Сумма введенных значений', result)
        numbers = (input('Введите числа').upper().split())