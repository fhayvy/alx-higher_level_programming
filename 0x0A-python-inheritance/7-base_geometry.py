#!/usr/bin/python3
"""Creates a class BaseGeometry"""


class BaseGeometry():
    """Creates a class BaseGeometry"""

    def area(self):
        """The method is not yet implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
