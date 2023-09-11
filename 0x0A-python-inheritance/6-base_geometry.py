#!/usr/bin/python3
"""This module contains the BaseGeometry class"""


class BaseGeometry:
    """A class for representing basic geometry"""

    def area(self):
        """Public instance method that raises an Exception with the message
        'area() is not implemented'"""
        raise Exception("area() is not implemented")
