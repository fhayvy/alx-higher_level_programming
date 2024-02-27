#!/usr/bin/python3
"""Inherits from base"""

from models.base import Base


class Rectangle(Base):
    """Creates a class Rectangle which inherits from the Base class"""

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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
