#!/usr/bin/python3
"""Base model for managing identifiers and serialization."""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances into a CSV file."""
        fields = ["id", "size", "x", "y"]
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        with open(cls.__name__ + ".csv", "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs or []:
                data = obj.to_dictionary()
                writer.writerow([data[key] for key in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        fields = ["id", "size", "x", "y"]
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        try:
            with open(cls.__name__ + ".csv", newline="") as file:
                reader = csv.reader(file)
                return [cls.create(**dict(zip(fields, map(int, row))))
                        for row in reader if row]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file."""
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs or []:
                data = obj.to_dictionary()
                writer.writerow([data[key] for key in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file."""
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as file:
                reader = csv.reader(file)
                return [cls.create(**dict(zip(fields, map(int, row))))
                        for row in reader if row]
        except FileNotFoundError:
            return []
