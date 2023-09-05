#!/usr/bin/python3
"""

This Python script defines the add_integer function,
which takes two arguments, and returns their sum as an integer

"""


def add_integer(a, b=98):
    """Adds two integers or floats as integers

    Args:
        a: The first integer or float to be added
        b: The second integer or float to be added

    Returns:
        The result of adding a and b as an integer

    Raises:
        TypeError: If either a or b is not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
