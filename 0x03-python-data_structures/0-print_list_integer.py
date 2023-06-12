#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(new_list=[]):
    """Print all integers of a list."""
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
