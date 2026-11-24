#!/usr/bin/python3
"""Find the maximum integer in a list."""


def max_integer(list=[]):
    """Return the largest integer in list, or None if list is empty."""
    if len(list) == 0:
        return None
    result = list[0]
    for value in list[1:]:
        if value > result:
            result = value
    return result
