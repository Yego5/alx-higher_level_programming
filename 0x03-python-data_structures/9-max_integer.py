#!/usr/bin/python3

def max_integer(inpt_list=[]):
    if not inpt_list:
        return None
    return sorted(inpt_list)[-1]
