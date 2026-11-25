#!/usr/bin/python3
"""Base model for managing identifiers and serialization."""
import json


class Base:
    """Base class for all geometric models."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance identifier."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionaries to a JSON string."""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Save instances to a JSON file."""
        data = [obj.to_dictionary() for obj in (list_objs or [])]
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from its dictionary representation."""
        obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                data = cls.from_json_string(file.read())
                return [cls.create(**item) for item in data]
        except FileNotFoundError:
            return []
