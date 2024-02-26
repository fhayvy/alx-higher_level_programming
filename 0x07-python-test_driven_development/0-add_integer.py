#!/usr/bin/python3
"""This Module adds two integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Raises:
        TypeError: If either of the arguments is not an integer or float

    Returns:
        The sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
