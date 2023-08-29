#!/usr/bin/python3
"""This module defines the Square class"""


class Square:
    """This is the Square class"""
    def __init__(self, size=0):
        """Initializes a new Square instance

        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size