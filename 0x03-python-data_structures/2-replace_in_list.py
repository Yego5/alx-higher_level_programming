#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(nw_list, nw_idx, nw_element):
    """Replace an element of a list at a specific position."""
    if nw_idx >= 0 and nw_idx < len(nw_list):
        nw_list[nw_idx] = nw_element
    return nw_list
