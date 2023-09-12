#!/usr/bin/python3
"""This module defines a function to write a string to a text file (UTF-8)
and return the number of characters written"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
