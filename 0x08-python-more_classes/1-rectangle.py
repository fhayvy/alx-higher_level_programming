#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Writes a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class object
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value: The value of the width
        Raises:
            ValueError: if value is less than 0
            TypeError: if value is not an int
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value: The value of the height
        Returns:
            ValueError: If value is less than 0
            TypeError: If value is not an int
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        self.__height = value
