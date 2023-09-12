#!/usr/bin/python3
"""This module defines a function to convert an object to its
JSON representation as a string"""
import json


def to_json_string(my_obj):
    """ Convert an object to its JSON representation as a string"""
    return json.dumps(my_obj)
