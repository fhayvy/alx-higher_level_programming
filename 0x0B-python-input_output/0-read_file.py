#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """Reads a textfile and prints out to stdout"""

    with open(filename, encoding="UTF8") as f:
        text = f.read()
        print(text)
