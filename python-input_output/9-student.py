#!/usr/bin/python3
"""Define a student object with JSON dictionary representation."""


class Student:
    """Represent a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the student."""
        return self.__dict__.copy()
