#!/usr/bin/python3
"""This module defines the LockedClass"""


class LockedClass:
    """
    LockedClass prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called 'first_name'.
    """
    def __setattr__(self, name, value):
        """
        Custom __setattr__ method to restrict attribute creation.

        Args:
            name (str): The name of the attribute being set.
            value (any): The value to assign to the attribute.

        Raises:
            AttributeError: If an attempt is made to create an attribute
                with a name other than 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError
        ("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
