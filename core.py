import sys


class TYPE_MAT:
    pass


class TYPE_SQRE_MAT:
    pass


class TYPE_AUG_MAT:
    pass


def raise_InvalidFormatError():
    print("[*] Invalid matrix format : Matrix should be in nested <list> "
          "format and cannot be empty \n    (e.g. : [[3, 1, '4'],[1, 5/9, 2]")
    sys.exit()


def raise_InvalidValueError(value):
    print("[*] Invalid value `{}` : Matrix entry should ".format(value) +
          "be either <int> or numeric <str>. \n    (e.g. : 3, '3', '3/5')")
    sys.exit()
