def personal():
    name = input('Введите имя')
    surname = input('Введите фамилию')
    bday = input('Введите день рождения')
    city = input('Введите город проживания')
    email = input('Введите электронную почту')
    phone = input('Введите контактный телефон')
    return name + ',' + surname + ',' + bday + ',' + city + ',' + email + ',' + phone
print(personal())