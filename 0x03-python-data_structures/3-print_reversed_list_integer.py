#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(nw_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(nw_list, list):
        nw_list.reverse()
        for i in nw_list:
            print("{:d}".format(i))
