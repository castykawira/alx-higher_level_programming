#!/usr/bin/python3
"""This module contains the BaseGeometry class"""


class BaseGeometry:
    """A class for representing basic geometry"""

    def area(self):
        """Public instance method that raises an Exception with the message
        'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates an integer value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
