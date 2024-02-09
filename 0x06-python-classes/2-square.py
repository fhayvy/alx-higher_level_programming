#!/usr/bin/python3
"""Defines a square"""


class Square:
    """The blueprint to create a sqaure"""

    def __init__(self,size=0):
        """Initializes the square
        Args: 
            size - Represnts the size of the square defined
        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not an integer
        """

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size
