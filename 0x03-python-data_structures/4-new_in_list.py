#!/usr/bin/python3

def new_in_list(my_list, ndx, element):
    new_list = my_list.copy()
    if 0 <= ndx < len(new_list):
        new_list[ndx] = element
    return new_list
