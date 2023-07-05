#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.rw = width
        self.ht = height

    @property
    def rw(self):
        """Get/set the width of the Rectangle."""
        return self.__rw

    @rw.setter
    def rw(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__rw = value

    @property
    def ht(self):
        """Get/set the height of the Rectangle."""
        return self.__ht

    @ht.setter
    def ht(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__ht = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__rw * self.__ht)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__rw == 0 or self.__ht == 0:
            return (0)
        return ((self.__rw * 2) + (self.__ht * 2))
