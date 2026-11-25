#!/usr/bin/python3
"""Module for printing squares using the hash character."""


def print_square(size):
    """Print a square of the specified integer size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
