#!/usr/bin/python3
"""Define the BaseGeometry class."""


class BaseGeometry:
    """Provide a base class for geometry objects."""

    def area(self):
        """Raise an exception because area calculation is unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Require value to be a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")