#!/usr/bin/python3
"""Inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle while inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
