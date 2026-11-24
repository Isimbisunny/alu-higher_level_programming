#!/usr/bin/python3
"""Print text with indentation after punctuation marks."""


def text_indentation(text):
    """Print text, adding two newlines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for character in text:
        if character in ".?:":
            print((line + character).strip())
            print()
            line = ""
        else:
            line += character
    remainder = line.strip()
    if remainder:
        print(remainder)
