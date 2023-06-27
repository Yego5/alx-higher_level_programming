#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for k in range(x):
            try:
                if isinstance(my_list[k], int):
                    print("{:d}".format(my_list[k]), end="")
                    count += 1
            except (ValueError, TypeError):
                pass
    except TypeError:
        return count
    print("")
    return count
