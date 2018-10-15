from matcalc.error import *
from fractions import Fraction


class Entry:
    # Define a number in a Fraction class format.
    def __init__(self, numerator, denominator=1):
        # Check if they are numbers
        self.value = Fraction(numerator, denominator)

    def __add__(self, other):
        frac = self.value + other.value
        return Entry(frac._numerator, frac._denominator)

    def __mul__(self, other):
        frac = self.value * other.value
        return Entry(frac._numerator, frac._denominator)

    def __str__(self):
        return str(self.value)


class Matrix:
    def __init__(self, matrix):
        # Check if matrix is in appropriate format
        self.check_matrix(matrix)
        self.convert_matrix(matrix)

    def convert_matrix(self, matrix):
        """
        This function is premised on the fact that all entries are convertible.
        """
        self.value = []

        for row in matrix:
            entry_row = []
            for entry in row:
                if type(entry) == int:
                    entry = Entry(entry)
                elif type(entry) == str:
                    entry = list(map(str.strip, entry.split('/')))
                    if len(entry) == 2:
                        # Fraction
                        entry = Entry(int(entry[0]), int(entry[1]))
                    elif len(entry) == 1:
                        # numeric <str>
                        entry = Entry(int(entry[0]))

                entry_row.append(entry)

            self.value.append(entry_row)

    def check_matrix(self, matrix):
        # Check if matrix is in appropriate format
        if type(matrix) != list:
            raise_error("Matrix should be in nested <list> format.")

        if len(matrix) == 0:
            raise_error("Matrix cannot be empty.")

        for row in matrix:
            if type(row) != list:
                raise_error("Matrix should be in nested <list> format.")
            for entry in row:
                if type(entry) == str:
                    entry = list(map(str.strip, entry.split('/')))
                    print(entry)
                    # Check if it is fraction <str>
                    if len(entry) == 2:
                        if not entry[0].isnumeric():
                            raise_error('Matrix entry should be in <int>.')
                        if not entry[1].isnumeric():
                            raise_error('Matrix entry should be in <int>.')

                    # Check if it is numeric <str>
                    elif len(entry) == 1:
                        try:
                            int(entry[0])
                        except TypeError:
                            raise_error('Matrix entry should be in <int>.')
                    else:
                        raise_error('Matrix entry should be in <int>')

                elif type(entry) != int:
                    raise_error('Matrix entry should be in ')


class SquareMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)


class AugmentedMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)
