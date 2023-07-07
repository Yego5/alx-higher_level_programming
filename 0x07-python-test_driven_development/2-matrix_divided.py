#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(new_matrix, divisor):
    """Divide all elements of a matrix.

    Args:
        new_matrix (list): A list of lists of ints or floats.
        divisor (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(new_matrix, list) or new_matrix == [] or
            not all(isinstance(row, list) for row in new_matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in new_matrix for num in row])):
        raise TypeError("new_matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(new_matrix[0]) for row in new_matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, int) and not isinstance(divisor, float):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / divisor, 2), row)) for row in new_matrix])
