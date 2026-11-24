#!/usr/bin/python3
"""Define a base geometry class with an area interface."""


class BaseGeometry:
    """Represent the base for geometry classes."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
