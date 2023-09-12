#!/usr/bin/python3
"""This module defines a function to append a string to the end of a text file
(UTF-8) and return the number of characters added"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF-8)
    and return the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
