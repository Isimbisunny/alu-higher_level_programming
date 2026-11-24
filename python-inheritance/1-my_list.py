#!/usr/bin/python3
"""Define a list subclass that can print its values in sorted order."""


class MyList(list):
    """A list with an append method and sorted printing."""

    def append(self, value):
        """Append value to the list using the standard list behavior."""
        super().append(value)

    def print_sorted(self):
        """Print the integers in ascending order without changing the list."""
        print(sorted(self))
