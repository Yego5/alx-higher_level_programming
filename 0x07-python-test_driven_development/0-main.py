#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(5, 7))
print(add_integer(200, -50))
print(add_integer(3))
print(add_integer(105.8, -2))
try:
    print(add_integer(6, "Chat"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
