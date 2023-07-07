#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(numbers=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(numbers) == 0:
        return None
    result = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > result:
            result = numbers[i]
        i += 1
    return result
