#!/usr/bin/python3
"""Divide every value in a matrix by a number."""


def matrix_divided(matrix, div):
    """Return a new matrix with values divided and rounded to 2 decimals."""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    size = len(matrix[0])
    if any(len(row) != size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if any(type(value) not in (int, float)
           for row in matrix for value in row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
