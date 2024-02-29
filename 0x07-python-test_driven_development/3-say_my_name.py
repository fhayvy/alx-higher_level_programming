#!/usr/bin/python3
"""This module contains a function which prints out the
first name and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """Prints out the first and last name of
    a person
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
