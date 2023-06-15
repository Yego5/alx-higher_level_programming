#!/usr/bin/python3

def search_replace(my_list, search, replace):
    th_list = my_list.copy()
    for i, item in enumerate(th_list):
        if item == search:
            th_list[i] = replace
    return th_list
