#!/usr/bin/python3
"""This module defines a MagicClass that performs various calculations."""

import math


class MagicClass:
    """
    This class represents MagicClass that can calculate area and circumference

    Attributes:
        __radius (float): The radius of the MagicClass instance.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (float): The radius value for the MagicClass instance.
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Retrieve the radius of the MagicClass instance."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the MagicClass instance.

        Args:
            value (float): The radius value to set.

        Raises:
            TypeError: If value is not a number.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Calculate the area of the MagicClass instance.

        Returns:
            float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the MagicClass instance.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
