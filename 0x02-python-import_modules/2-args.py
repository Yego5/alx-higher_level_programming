#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from the arguments

    count = len(args)
    if count == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif count == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(args[0]))
    else:
        print("Number of argument(s): {}.".format(count))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
