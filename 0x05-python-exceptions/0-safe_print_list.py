#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for k in range(x):
            print("{}".format(my_list[k]), end="")
            total += 1
    except IndexError:
        pass
    print("")
    return total
