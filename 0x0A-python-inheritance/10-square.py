#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
