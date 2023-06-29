#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, sz=0):
        """Initialize a new square.

        Args:
            sz (int): The size of the new square.
        """
        self.sz = sz

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

    def area(self):
        """Return the current area of the square."""
        return self.__sz * self.__sz

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()
