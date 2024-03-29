#!/usr/bin/python3
"""A base class"""


class Base():
    """Creates the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
