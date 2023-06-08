#!/usr/bin/python3

for character in range(ord('a'), ord('z') + 1):
    if character != 101 and character != 113:
        print("{:c}".format(character), end='')

print()

