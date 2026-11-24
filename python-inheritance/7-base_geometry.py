#!/usr/bin/python3
"""Define the BaseGeometry class."""


class BaseGeometry:
    """Provide a base class for geometry objects."""

    def area(self):
        """Raise an exception when no area implementation is provided."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Require value to be a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
