#!/usr/bin/python3
"""Checks if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance
    of or a class that inherited from
    """

    return (isinstance(obj, a_class))
