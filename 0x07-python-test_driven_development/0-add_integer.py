#!/usr/bin/python3
# 0-add_integer.py
# festus sulumeti
""" File name : 0-add_integer.py
    Integers addition: function that adds 2 integers
    Prototype: def add_integer(a, b=98)
    You are not allowed to import any module
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
