#!/usr/bin/python3
"""Define a square based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square and inherit rectangle behavior."""

    def __init__(self, size):
        """Initialize a square with a positive integer size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
