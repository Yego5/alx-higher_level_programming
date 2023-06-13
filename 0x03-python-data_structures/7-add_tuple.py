#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    itm_a = [0, 0]
    itm_b = [0, 0]

    if len(tuple_a) >= 2:
        itm_a = tuple_a[:2]
    elif len(tuple_a) == 1:
        itm_a[0] = tuple_a[0]

    if len(tuple_b) >= 2:
        itm_b = tuple_b[:2]
    elif len(tuple_b) == 1:
        itm_b[0] = tuple_b[0]

    return tuple((itm_a[x] + itm_b[x]) for x in range(2))
