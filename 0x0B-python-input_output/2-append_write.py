#!/usr/bin/python3
"""Writes a string to a text file"""


def append_write(filename="", text=""):
    """Returns the number of characters written"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
