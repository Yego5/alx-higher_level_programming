#!/usr/bin/python3
def print_matrix_integer(nw_matrix=[[]]):
	for nw_row in nw_matrix:
    	for nw_col in nw_row:
        	print("{:d}".format(nw_col), end=" " if nw_col != nw_row[-1] else "")
    	print()
