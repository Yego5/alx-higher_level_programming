#!/usr/bin/python3
def square_matrix_simple(mtrx=[]):
    squared = []
    for rw in mtrx:
        squared.append([el**2 for el in rw])
    return squared
