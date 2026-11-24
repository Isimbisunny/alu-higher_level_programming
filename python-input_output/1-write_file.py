#!/usr/bin/python3
"""Write text to a UTF-8 file and report its character count."""


def write_file(filename="", text=""):
    """Overwrite filename with text and return the characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
