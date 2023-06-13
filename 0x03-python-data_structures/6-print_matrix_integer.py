#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rw in matrix:
            if rw:
                for idx, clm in enumerate(rw):
                    if idx == (len(rw) - 1):
                        print("{:d}".format(clm))
                    else:
                        print("{:d}".format(clm), end=" ")
            else:
                print()
