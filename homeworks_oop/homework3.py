def hcf(a, b):
    if a == 0:
        return b
    else:
        return hcf(b % a, a)

class Fraction:

    def __init__(self, numertor, denumerator):
        hcf1 = hcf(numertor, denumerator)
        self.numertor = numertor // hcf1
        self.denumerator = denumerator // hcf1

    def __str__(self):
        if self.denumerator == 1:
            return str(self.numertor)

        elif self.numertor > self.denumerator:
            return str(self.numertor // self.denumerator) + " " +\
                   str(Fraction(self.numertor % self.denumerator, self.denumerator))
        else:
            return str(self.numertor) + "/" + str(self.denumerator)

    def __add__(self, other):
        new_numertor = self.numertor * other.denumerator + other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __sub__(self, other):
        new_numertor = self.numertor * other.denumerator - other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __mul__(self, other):
        new_numertor = self.numertor * other.numertor
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __floordiv__(self, other):
        new_numertor = self.numertor // other.numertor
        new_denumerator = self.denumerator // other.denumerator
        return Fraction(new_numertor, new_denumerator)

a = Fraction(3, 9)
b = Fraction(1, 3)

print(a + b)
print(a - b)
print(a * b)
print(a // b)