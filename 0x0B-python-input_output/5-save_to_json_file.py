#!/usr/bin/python3
"""This module defines a function to save an object to a text file in
JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to a text file in JSON format"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
