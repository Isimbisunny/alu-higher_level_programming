#!/usr/bin/python3
"""Provide class and inheritance instance checking."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or one of its subclasses."""
    return isinstance(obj, a_class)
