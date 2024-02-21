#!/usr/bin/python3
"""Inherits from int"""


class MyInt(int):
    """A class MyInt that inherits from int"""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""

        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""

        return self.real == value
