#!/usr/bin/python3
"""Define a student supporting JSON serialization and reloading."""


class Student:
    """Represent a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return all or selected public attributes of the student."""
        if type(attrs) is list:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace the student's attributes using values from json."""
        for key, value in json.items():
            setattr(self, key, value)
