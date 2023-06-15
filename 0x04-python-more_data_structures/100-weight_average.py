#!/usr/bin/python3
def weight_average(n_list=[]):
    if not n_list:
        return 0

    num = 0
    den = 0

    for n_tuple in n_list:
        num += n_tuple[0] * n_tuple[1]
        den += n_tuple[1]

    return (num / den)
