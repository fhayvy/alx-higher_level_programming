#!/usr/bin/python3
"""Defines a Student"""


class Student():
    """Creates a student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""

        return self.__dict__
