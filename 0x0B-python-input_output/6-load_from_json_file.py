#!/usr/bin/python3
"""This script provides functions to work with JSON files"""
import json


def load_from_json_file(filename):
    """Load an object from a JSON file"""
    with open(filename) as file:
        return json.load(file)
