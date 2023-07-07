#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function."""


def say_my_name(name, surname=""):
    """Print a name.

    Args:
        name (str): The name to print.
        surname (str): The surname to print.
    Raises:
        TypeError: If either of name or surname are not strings.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(surname, str):
        raise TypeError("surname must be a string")
    print("My name is {} {}".format(name, surname))
