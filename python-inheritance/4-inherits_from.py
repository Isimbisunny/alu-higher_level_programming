#!/usr/bin/python3
"""Provide inherited-only class checking."""


def inherits_from(obj, a_class):
    """Return whether obj inherits from a_class, not by exact class match."""
    return isinstance(obj, a_class) and type(obj) is not a_class
