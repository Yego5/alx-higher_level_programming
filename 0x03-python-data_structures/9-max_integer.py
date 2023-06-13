#!/usr/bin/python3
# 9-max_integer.py

def max_integer(inpt_list=[]):
    """Find the biggest integer of a list."""
    if len(inpt_list) == 0:
        return None

    max_value = inpt_list[0]
    for i in range(len(inpt_list)):
        if inpt_list[i] > max_value:
            max_value = inpt_list[i]

    return max_value
