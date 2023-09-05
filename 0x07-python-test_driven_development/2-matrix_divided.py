#!/usr/bin/python3
"""

This module defines a Python function matrix_divided

"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor

    Args:
        matrix: The input matrix, a list of lists containing integers or floats
        div: The divisor used for division
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: if each row of the matrix does not have the same size
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    Returns:
        A new matrix where all elements are divided by div
        and rounded to 2 decimal places
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
