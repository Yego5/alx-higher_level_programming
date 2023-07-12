#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, class_to_check):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        class_to_check (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of class_to_check - True.
        Otherwise - False.
    """
    if issubclass(type(obj), class_to_check) and type(obj) != class_to_check:
        return True
    return False
