#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Blueprint to create a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square object
        Args:
            size: The value of the size
            position: A tuple of 2 positive integers
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of the square"""

        return (self.__size)

    @property
    def position(self):
        """Retrieves the position"""

        return (self.__position)

    @size.setter
    def size(self, value):
        """Sets the value of the size
        Args:
            value: The size of the square
        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not an int
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position
        Args:
            value: The position of the tuple
        Raises:
            TypeError: If value is not a tuple or any int in tuple < 0
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """Calculates the area of the square
        Returns the Area
        """

        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()