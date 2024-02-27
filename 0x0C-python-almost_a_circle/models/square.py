#!/usr/bin/python3
"""Inherits from rectangle.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class"""

        self.__size = size
        self.__x = x
        self.__y = y
        self.id = None

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}")
