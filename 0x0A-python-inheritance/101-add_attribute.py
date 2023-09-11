#!/usr/bin/python3
"""This function adds a new attribute to an object if it's possible.
If the object can't have a new attribute, it raises a TypeError"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
