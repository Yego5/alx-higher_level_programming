#!/usr/bin/python3
# 1-element_at.py

def element_at(new_list, new_idx):
    """Retrieve an element from a list."""
    if new_idx < 0 or new_idx > (len(new_list) - 1):
        return None
    return new_list[new_idx]
