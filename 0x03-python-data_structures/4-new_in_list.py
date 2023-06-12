#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(new_list, new_idx, new_element):
    """Replace an element in a copied list at a specific position."""
    if new_idx < 0 or new_idx > (len(new_list) - 1):
        return new_list

    copy = [x for x in new_list]
    copy[new_idx] = new_element
    return copyy
