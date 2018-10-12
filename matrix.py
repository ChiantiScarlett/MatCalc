class Entry:
    # Define a number in a class format.
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __str__(self):
        if self.denominator == 1:
            return self.numerator
        else:
            return '{} / {}'.format(self.numerator, self.denominator)


class Matrix:
    def __init__(self, *args, **kwargs):
        pass


class SquareMatrix(Matrix):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class AugmentedMatrix(Matrix):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
