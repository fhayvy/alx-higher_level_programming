#!/usr/bin/python3
"""Inherits from base"""

from models.base import Base


class Rectangle(Base):
    """Creates a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle class"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width value"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Gets the x value"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Gets the y value"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the rectangle"""

        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(width):
            pass
        pass

    def __str__(self):
        """Overrides the __str__ method"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
