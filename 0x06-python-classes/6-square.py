#!/usr/bin/python3
class Square:

    def __init__(self,size=0, position=(0, 0)):
        self.__size = size
        self.__position = position


    @property
    def size(self):
        return (self.__size)


    @property
    def position(self):
        return (self.__position)


    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = value


    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position


    def area(self):
        return (self.__size ** 2)


    def my_print(self):
        if self.__size == 0:
            print()
