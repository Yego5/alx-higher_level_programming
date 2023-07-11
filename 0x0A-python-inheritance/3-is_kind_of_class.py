#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, class_to_check):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        class_to_check (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of class_to_check - True.
        Otherwise - False.
    """
    if isinstance(obj, class_to_check):
        return True
    return False
