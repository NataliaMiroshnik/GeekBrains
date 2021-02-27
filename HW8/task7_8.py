class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print((self.a + other.a), '+', (self.b + other.b), 'i')

    def __mul__(self, other):
        print((self.a * other.a), '+', (self.b * other.b), 'i')

complex_1 = Complex(5,9)
complex_2 = Complex(2,8)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
