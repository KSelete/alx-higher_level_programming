#!/usr/bin/python3
"""
Fucntion that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

    Matrix must be a list of lists
    of integers, floats.
    Return: a new matrix
    """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    div1 = "div must be a number"
    div2 = "division by zero"

    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError(err1)
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(err1)
        if len(matrix[0]) is not len(element):
            raise TypeError(err2)
        for j in element:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(err1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(div1)
    if div is 0:
        raise ZeroDivisionError(div2)

    return[[round(j / div, 2) for j in i] for i in matrix]
