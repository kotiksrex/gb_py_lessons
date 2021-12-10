class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i' if self.b > 0 else f'{self.a}{self.b}i'

    def __add__(self, other):
        print(f'Сумма a и b равна')
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print(f'Произведение a и b равно')
        return ComplexNumber((self.a * other.a - self.b * other.b),
                             (self.b * other.a + self.a * other.b))


x = ComplexNumber(1, -2)
y = ComplexNumber(3, 4)
print(x + y)
print(x * y)
