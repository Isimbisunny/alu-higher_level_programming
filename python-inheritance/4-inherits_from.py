#!/usr/bin/python3
"""Provide inherited-only class checking."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class without being the exact class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
