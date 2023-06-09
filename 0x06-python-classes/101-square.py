#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, sz=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            sz (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.sz = sz
        self.position = position

    @property
    def sz(self):
        """Get/set the current size of the square."""
        return self.__sz

    @sz.setter
    def sz(self, value):
        if not isinstance(value, int):
            raise TypeError("sz must be an integer")
        elif value < 0:
            raise ValueError("sz must be >= 0")
        self.__sz = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__sz * self.__sz

    def my_print(self):
        """Print the square with the # character."""
        if self.__sz == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__sz):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__sz)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__sz != 0:
            [print("") for _ in range(self.__position[1])]
        for _ in range(self.__sz):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__sz)]
            if _ != self.__sz - 1:
                print("")
        return ""
