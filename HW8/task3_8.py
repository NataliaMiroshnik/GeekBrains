my_list = []
element = input('Введите новый элемент списка')
while element != 'stop':
    if not element.isdigit():
        print('Вы ввели не число')
        element = input('Введите новый элемент списка, который будет являться ЧИСЛОМ')
    else:
        my_list.append(element)
        element = input('Введите новый элемент списка')
print(my_list)
