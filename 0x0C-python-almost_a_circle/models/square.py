#!/usr/bin/python3
"""Inherits from rectangle.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class"""

        self.size = size
        self.x = x
        self.y = y
        self.id = None

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size value"""

        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        """Defines a string representation of the class"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
