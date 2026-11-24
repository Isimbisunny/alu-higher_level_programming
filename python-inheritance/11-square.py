#!/usr/bin/python3
"""Define a square with square-specific string output."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square and inherit rectangle behavior."""

    def __init__(self, size):
        """Initialize a square with a positive integer size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
