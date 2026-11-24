#!/usr/bin/python3
"""Print a square using the hash character."""


def print_square(size):
    """Print a square of size size using the # character."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
