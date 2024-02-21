#!/usr/bin/python3
"""Inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square while inheriting from Rectangle"""

    def __init__(self, size):
        """Initializes a square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)
