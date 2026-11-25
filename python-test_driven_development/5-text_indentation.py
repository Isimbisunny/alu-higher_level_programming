#!/usr/bin/python3
"""Module for formatting text with indentation."""


def text_indentation(text):
    """Print text with two newlines after specified punctuation."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char in ".?:":
            print((line + char).strip(), end="\n\n")
            line = ""
        elif char == "\n":
            print(line.strip())
            line = ""
        else:
            line += char
    print(line.strip(), end="")
