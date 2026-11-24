#!/usr/bin/python3
"""Generate Pascal's triangle rows."""


def pascal_triangle(n):
    """Return Pascal's triangle with n rows as a list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]
    for row_index in range(1, n):
        previous = triangle[-1]
        row = [1]
        for index in range(1, row_index):
            row.append(previous[index - 1] + previous[index])
        row.append(1)
        triangle.append(row)
    return triangle
