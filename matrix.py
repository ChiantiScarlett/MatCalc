from matcalc.core import raise_InvalidValueError, raise_InvalidFormatError

from fractions import Fraction


class Entry:
    # Define a number in a Fraction class format.
    def __init__(self, value):
        # Raise error if the value is in invalid format.
        # Examples of valid format are 1 , '1' , '2/3'
        # Invalid formats can be 1/3 , 1.6 , [3]

        if type(value) == int:
            self.value = Fraction(value)
        elif type(value) != str:
            raise_InvalidValueError(value)
        elif value.isnumeric():
            self.value = Fraction(int(value))
        elif len(value.split('/')) != 2:
            raise_InvalidValueError(value)
        else:
            numer, denom = list(map(str.strip, value.split('/')))
            if not (numer.isnumeric() and denom.isnumeric()):
                raise_InvalidValueError(value)

            self.value = Fraction(int(numer), int(denom))

    def _simplify_fraction(self, frac):
        """
        Since Fraction does not always simplifies the fraction, this method is
        necessary for addition and multiplication among Fractions.
        """

        # Euclid Method of getting GCD
        numer = frac._numerator
        denom = frac._denominator

        while denom:
            numer, denom = denom, numer % denom
        gcd = numer

        numer = int(frac._numerator / gcd)
        denom = int(frac._denominator / gcd)

        return Entry('{} / {}'.format(numer, denom))

    def __add__(self, other):
        return self._simplify_fraction(self.value + other.value)

    def __mul__(self, other):
        return self._simplify_fraction(self.value * other.value)

    def __str__(self):
        return str(self.value)


class Matrix:
    def __init__(self, matrix):
        # Check if matrix is in appropriate format
        self._check_matrix(matrix)
        self._convert_matrix(matrix)

    def _convert_matrix(self, matrix):
        """
        This function is premised on the fact that all entries are convertible.
        """
        self.value = []
        self._row_num = len(matrix)
        self._col_num = len(matrix[0])

        for row in matrix:
            entry_row = []
            for entry in row:
                entry_row.append(Entry(entry))

            self.value.append(entry_row)

    def _check_matrix(self, matrix):
        # Check if matrix is in appropriate format
        if type(matrix) != list:
            raise_InvalidFormatError()

        if len(matrix) == 0:
            raise_InvalidFormatError()

        col_num = len(matrix[0])

        for row in matrix:
            if len(row) != col_num:
                raise_InvalidFormatError()

    def transpose(self):
        """
        Transpose entries
        """
        new_value = []
        for col in range(len(self.value[0])):
            new_row = []
            for row in self.value:
                new_row.append(row[col])
            new_value.append(new_row)

        self.value = new_value
        self._row_num, self._col_num = self._col_num, self._row_num  # swap

    def show(self):
        # Find out maximum length of entries string
        max_length = 0
        for row in self.value:
            for entry in row:
                if len(str(entry)) + 2 > max_length:
                    max_length = len(str(entry)) + 2

        # Format
        text = []
        text.append('< {}, {} x {} >'.format('Matrix',
                                             self._row_num,
                                             self._col_num))

        for row in self.value:
            entry_line = " "
            for entry in row:
                entry_str = str(entry) + " " * (max_length - len(str(entry)))
                entry_line += entry_str
            text.append(entry_line)

        text = "\n\n".join(text)
        print(text)
