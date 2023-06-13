#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(nw_tuple_a=(), nw_tuple_b=()):
	"""Add two tuples."""
	if len(nw_tuple_a) < 2:
    	if len(nw_tuple_a) == 0:
        	nw_tuple_a = 0, 0
    	else:
        	nw_tuple_a = nw_tuple_a[0], 0
	if len(nw_tuple_b) < 2:
    	if len(nw_tuple_b) == 0:
        	nw_tuple_b = 0, 0
    	else:
        	nw_tuple_b = nw_tuple_b[0], 0

	return (nw_tuple_a[0] + nw_tuple_b[0], nw_tuple_a[1] + nw_tuple_b[1])
