#!/usr/bin/python3
"""Defines a square"""


class Square:
    """The blueprint for creating a square"""

    def __init__(self, size=0):
        """Initailizes the square class
        Args:
            size - The size of the square
        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not integer
        """

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        """Calulates the area of the square
        Returns: The value of the area"""

        return (self.__size ** 2)
