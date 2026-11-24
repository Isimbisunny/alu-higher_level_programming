#!/usr/bin/python3
"""Provide a function for listing an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of obj."""
    return dir(obj)
