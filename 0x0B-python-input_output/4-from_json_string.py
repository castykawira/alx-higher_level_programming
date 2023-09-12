#!/usr/bin/python3
"""This module defines a function to convert a JSON string
to a Python data structure"""


import json


def from_json_string(my_str):
    """Convert a JSON string to a Python data structure (object)"""
    return json.loads(my_str)
