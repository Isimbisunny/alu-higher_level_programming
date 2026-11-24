#!/usr/bin/python3
"""Load Python objects from JSON text files."""
import json


def load_from_json_file(filename):
    """Read filename and return its represented Python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
