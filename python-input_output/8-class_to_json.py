#!/usr/bin/python3
"""Convert a simple object's public attributes to a dictionary."""


def class_to_json(obj):
    """Return obj.__dict__, containing its public and private instance data."""
    return obj.__dict__.copy()
