#!/usr/bin/python3
"""Define a list subclass that can print its values in sorted order."""


class MyList(list):
    """A list with a method for printing a sorted copy."""

    def print_sorted(self):
        """Print the integers in ascending order without changing the list."""
        print(sorted(self))
