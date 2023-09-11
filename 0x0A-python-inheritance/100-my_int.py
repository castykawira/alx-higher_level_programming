#!/usr/bin/python3
"""MyInt class that inherits from int with inverted == and != operators"""


class MyInt(int):
    """MyInt class that inherits from int with inverted == and != operators"""

    def __eq__(self, value):
        """Override the == operator"""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator"""
        return self.real == value
