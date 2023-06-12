#!/usr/bin/python3
# 4-nw_in_list.py

def nw_in_list(nw_list, nw_idx, nw_element):
	"""Replace an element in a copied list at a specific position."""
	if nw_idx < 0 or nw_idx > (len(nw_list) - 1):
    		return nw_list

	copy = [x for x in nw_list]
	copy[nw_idx] = nw_element
	return copy
