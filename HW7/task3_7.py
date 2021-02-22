class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f"{self.quantity + other.quantity}"

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return f"{self.quantity - other.quantity}"
        else:
            return 'Невозможно из меньшего вычесть большее'

    def __mul__(self, other):
        return f"{self.quantity * other.quantity}"

    def __truediv__(self, other):
        return f"{self.quantity // other.quantity}"

    def make_order(self):
        a = self.quantity // 5
        b = self.quantity % 5
        result = ''
        while a != 0:
            result += '*****\n'
            a -=1
        result += '*'*b
        print(result)

cell_1 = Cell(78)
cell_2 = Cell(88)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order())