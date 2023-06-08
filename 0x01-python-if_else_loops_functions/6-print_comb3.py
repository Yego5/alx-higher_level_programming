#!/usr/bin/python3
for nam1 in range(0, 10):
for nam2 in range(nam1 + 1, 10):
    if nam1 == 8 and nam2 == 9:
        print("{}{}".format(nam1, nam2))
    else:
        print("{}{}".format(nam1, nam2), end=", ")
