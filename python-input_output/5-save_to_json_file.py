#!/usr/bin/python3
"""Save Python objects as JSON in text files."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of my_obj to filename."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
