#!/usr/bin/python3
"""Defines a class"""


class Square:
    """Blueprint for creating a square"""

    def __init__(self, size=0):
        """Initializes the square object
        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """A getter to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size
        Args:
            value: The size of the square
        Returns:
            ValueError: If size is less than 0
            TypeError: If size is not an integer
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = value

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

    def __eq__(self, other):

        return self.area() == other.area()

    def __ne__(self, other):

        return self.area() != other.area()

    def __ge__(self, other):

        return self.area() >= other.area()

    def __gt__(self, other):

        return self.area() > other.area()

    def __le__(self, other):

        return self.area() <= other.area()

    def __lt__(self, other):

        return self.area() < other.area()
