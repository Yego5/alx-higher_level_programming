#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for argmt in sys.argv:
        if argmt != sys.argv[0]:
            total += int(argmt)
    print(total)
