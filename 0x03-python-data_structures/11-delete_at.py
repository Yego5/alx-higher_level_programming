#!/usr/bin/python3
# 11-delete_at.py


def delete_at(nw_list=[], nw_idx=0):
    """Delete an item at a specific position in a list."""
    if nw_idx >= 0 and nw_idx < len(nw_list):
        del nw_list[nw_idx]
    return nw_list
