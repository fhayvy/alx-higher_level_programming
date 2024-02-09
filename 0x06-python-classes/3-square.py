#!/usr/bin/python3
class Square:
    def __init__(self,size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
