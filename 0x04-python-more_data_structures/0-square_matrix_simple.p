#!/usr/bin/python3

def square_matrix_simple(mtrx=[]):
    if not mtrx:
        return mtrx

    squared_mtrx = [square_array(r.copy()) for r in mtrx]
    # squared_mtrx = list(map(square_array, mtrx.copy()))
    return squared_mtrx


def square_array(arr):
    return [i**2 for i in arr]
