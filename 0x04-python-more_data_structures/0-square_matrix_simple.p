#!/usr/bin/python3
def square_matrix_simple(mtrx=[]):
    return [list(map((lambda x: x * x), elmnt)) for elmnt in mtrx]
