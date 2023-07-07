#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(6)
print("")
print_square(12)
print("")
print_square(2)
print("")
print_square(3)
print("")
try:
    print_square(-2)
except Exception as e:
    print(e)
print("")
