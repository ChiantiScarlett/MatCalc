from fractions import Fraction


class Entry:
    # Define a number in a Fraction class format.
    def __init__(self, numerator, denominator=1):
        self.value = Fraction(numerator, denominator)

    def __add__(self, other):
        frac = self.value + other.value
        return Entry(frac._numerator, frac._denominator)

    def __mul__(self, other):
        frac = self.value * other.value
        return Entry(frac._numerator, frac._denominator)

    def __str__(self):
        return self.value.__str__()


class Matrix:
    def __init__(self, *args, **kwargs):
        pass


class SquareMatrix(Matrix):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class AugmentedMatrix(Matrix):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
