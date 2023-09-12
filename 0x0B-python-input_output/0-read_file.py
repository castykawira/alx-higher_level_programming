#!/usr/bin/python3
"""This module defines a function to read and print the content of a text file
(UTF-8) to stdout"""


def read_file(filename=""):
    """Read and print the content of a text file to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
