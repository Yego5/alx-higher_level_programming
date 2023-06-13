#!/usr/bin/python3
def print_matrix_integer(new_matrix=[[]]):
    for new_row in new_matrix:
        for new_col in new_row:
            print("{:d}".format(new_col), end=" " if new_col != new_row[-1] else "")
    print()
