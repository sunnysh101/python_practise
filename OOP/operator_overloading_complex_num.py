class Complex:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"({self.real}, {self.imag})"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

c3 = c1 + c2
print(c3)
