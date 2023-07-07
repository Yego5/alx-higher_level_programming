#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(side_length):
    """Print a square with the # character.

    Args:
        side_length (int): The side length of the square.
    Raises:
        TypeError: If side_length is not an integer.
        ValueError: If side_length is < 0
    """
    if not isinstance(side_length, int):
        raise TypeError("side_length must be an integer")
    if side_length < 0:
        raise ValueError("side_length must be >= 0")

    for i in range(side_length):
        [print("#", end="") for j in range(side_length)]
        print("")
