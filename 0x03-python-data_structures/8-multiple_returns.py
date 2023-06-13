#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(nw_sentence):
	"""Returns the length of a string and its first character."""
	if nw_sentence == "":
    	return (0, None)
	return (len(nw_sentence), nw_sentence[0])
