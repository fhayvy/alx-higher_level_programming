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

        self.__width = value

    @property
    def height(self):
        """Gets the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""

        self.__height = value

    @property
    def x(self):
        """Gets the x value"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""

        self.__x = value

    @property
    def y(self):
        """Gets the y value"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""

        self.__y = value
