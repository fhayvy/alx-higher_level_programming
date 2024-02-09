#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Blueprint for creating Square objects"""

    def __init__(self, size=0):
        """Initailizes the square
        Args:
            size: The size of the square
        """

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of the size
        Args:
            value: The size of the square
        Raises:
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
        """Returns The area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
