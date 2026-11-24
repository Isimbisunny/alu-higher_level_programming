#!/usr/bin/python3
"""Convert JSON strings to Python objects."""
import json


def from_json_string(my_str):
    """Return the Python object represented by my_str."""
    return json.loads(my_str)
