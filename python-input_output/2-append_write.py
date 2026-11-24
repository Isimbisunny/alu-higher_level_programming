#!/usr/bin/python3
"""Append text to a UTF-8 file and report its character count."""


def append_write(filename="", text=""):
    """Append text to filename and return the characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
