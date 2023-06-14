#!/usr/bin/python3
def square_matrix_simple(mtrx=[]):
    squared_matrix = []
    for line in mtrx:
        squared_matrix.append([c**2 for c in line])
    return squared_matrix
