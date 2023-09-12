#!/usr/bin/python3

"""
This script adds command line arguments to a list and saves it to a JSON file.
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items():
    """Check if the JSON file exists, and load its content if it does"""
    file_name = "add_item.json"

    if os.path.exists(file_name):
        my_list = load_from_json_file(file_name)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, file_name)


    add_items()
