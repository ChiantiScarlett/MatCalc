from matcalc.error import raise_InvalidValueError, raise_InvalidFormatError
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
        self._row_num = len(matrix)
        self._col_num = len(matrix[0])

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
            raise_InvalidFormatError()

        if len(matrix) == 0:
            raise_InvalidFormatError()

        for row in matrix:
            if type(row) != list:
                raise_InvalidFormatError()
            for entry in row:
                if type(entry) == str:
                    f_entry = list(map(str.strip, entry.split('/')))
                    # Check if it is fraction <str>
                    if len(f_entry) == 2:
                        if not f_entry[0].isnumeric():
                            raise_InvalidValueError(f_entry[0])
                        if not f_entry[1].isnumeric():
                            raise_InvalidValueError(f_entry[1])

                    # Check if it is numeric <str>
                    elif len(f_entry) == 1:
                        try:
                            int(f_entry[0])
                        except TypeError:
                            raise_InvalidValueError(entry)
                    else:
                        raise_InvalidValueError(entry)

                elif type(entry) != int:
                    raise_InvalidValueError(entry)

    def show(self):
        # Find out maximum length of entries string
        max_length = 0
        for row in self.value:
            for entry in row:
                if len(str(entry)) + 2 > max_length:
                    max_length = len(str(entry)) + 2

        # Format
        text = []
        text.append('< Matrix, {} x {} >'.format(self._row_num,
                                                 self._col_num))

        for row in self.value:
            entry_line = " "
            for entry in row:
                entry_str = str(entry) + " " * (max_length - len(str(entry)))
                entry_line += entry_str
            text.append(entry_line)

        text = "\n\n".join(text)
        print(text)


class SquareMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)


class AugmentedMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)
