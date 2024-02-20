#!/usr/bin/python3
"""A module that returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Returns:
        True: If the object is exactly an instance of the specified class
        False: If otherwise
    """

    return (isinstance(obj, a_class))
