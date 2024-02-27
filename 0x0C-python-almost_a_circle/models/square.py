#!/usr/bin/python3
"""Inherits from rectangle.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class"""

        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
