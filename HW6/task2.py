class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        weight = int(input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см '))
        thickness = int(input('Введите толщину полотна дороги'))
        length = self._length
        width = self._width
        print((length * width * weight * thickness/1000), 'тонн')
m4 = Road(20, 5000)
print(m4.weight_of_asphalt())