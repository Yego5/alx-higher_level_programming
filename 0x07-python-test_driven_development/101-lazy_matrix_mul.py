#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_multiply(matrix_a, matrix_b):
    """Return the multiplication of two matrices.

    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(matrix_a, matrix_b))
