#!/usr/bin/python3
"""

This python script contains a function Prints a square
with the character '#' of the given size

"""


def print_square(size):
    """Prints a square with the character '#' of the given size

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than 0
        ValueError: If size is less than 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for j in range(0, size):
        for k in range(size):
            print("#", end="")
        print("")
