#!/usr/bin/python3
def print_sorted_dictionary(n_dict):
    for p in sorted(n_dict.keys()):
        print("{}: {}".format(p, n_dict[p]))
