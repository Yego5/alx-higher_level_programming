#!/usr/bin/python3
def complex_delete(dct, value):
    tmp = dct.copy()
    for k, v in tmp.items():
        if value == v:
            dct.pop(k)
    return dct
