#!/usr/bin/python3
"""Creates a class BaseGeometry"""


class BaseGeometry():
    """Creates a class BaseGeometry"""

    def area(self):
        """The method is not yet implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value to see if it's an integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creates a rectangle while inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
