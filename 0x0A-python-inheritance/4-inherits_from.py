#!/usr/bin/python3
"""This module contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """Check if an object's class is a subclass of the specified class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
