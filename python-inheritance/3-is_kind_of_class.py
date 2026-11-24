#!/usr/bin/python3
"""Provide class and inheritance instance checking."""


def is_kind_of_class(obj, a_class):
    """Return whether obj is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
