#!/usr/bin/python3
"""
0-add_integer adds two integers
a and b must be integers or float
otherwise raise TypeError
float must be converted to int
"""


def add_integer(a, b=98):
    """
    Add two integers"

    Parameters:
    a is the first parameter
    b is the second parameter, if is empty takes the value of 98
    Returns: The addition of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
