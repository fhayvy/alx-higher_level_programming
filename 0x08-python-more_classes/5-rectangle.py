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

        self.width = width
        self.height = height

    def __del__(self):
        print("Bye rectangle...")

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

    def area(self):
        """Calculates the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""

        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return (perimeter)

    def __str__(self):
        """Prints the rectangle with the character #"""

        rec_string = ""

        if self.width == 0 or self.height == 0:
            return rec_string

        for i in range(self.height):
            for j in range(self.width):
                rec_string += '#'
            if i is not (self.height - 1):
                rec_string += '\n'
        return rec_string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
