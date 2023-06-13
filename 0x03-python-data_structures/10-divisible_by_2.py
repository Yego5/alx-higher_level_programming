#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(nw_list=[]):
	"""Find all multiples of 2 in a list."""
	multiples = []
	for i in range(len(nw_list)):
    	if nw_list[i] % 2 == 0:
        	multiples.append(True)
    	else:
        	multiples.append(False)

	return multiples
