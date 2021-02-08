text = input('Введите слово на латинице')
while text.isalpha() == False:
    text = input('Введите слово на латинице')
def int_func(text):
    return text.title()
print(int_func(text))