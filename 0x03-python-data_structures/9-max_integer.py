#!/usr/bin/python3
# 9-max_integer.py


def max_integer(nw_list=[]):
	"""Find the biggest integer of a list."""
	if len(nw_list) == 0:
    	return None

	big = nw_list[0]
	for k in range(len(nw_list)):
    	if nw_list[k] > big:
        	big = nw_list[k]

	return big
