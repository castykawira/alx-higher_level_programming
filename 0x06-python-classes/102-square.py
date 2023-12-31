#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize the square"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare squares for equality based on area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare squares for inequality based on area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare squares for greater than based on area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare squares for greater than or equal based on area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare squares for less than based on area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare squares for less than or equal based on area"""
        return self.area() <= other.area()
