#!/usr/bin/python3
"""Read and print the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Print the complete contents of filename to standard output."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
