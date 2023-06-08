#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("G is {}".format("lower" if islower("G") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("4 is {}".format("lower" if islower("4") else "upper"))
print("h is {}".format("lower" if islower("h") else "upper"))
