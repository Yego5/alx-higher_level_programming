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
        self._width = width  # Changed from self.width to self._width
        self._height = height  # Changed from self.height to self._height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value  # Changed from self.__width to self._width

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value  # Changed from self.__height to self._height

    def area(self):
        """Return the area of the Rectangle."""
        return self._width * self._height  # Changed from self.__width to self._width and self.__height to self._height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:  # Changed from self.__width to self._width and self.__height to self._height
            return 0
        return (self._width * 2) + (self._height * 2)  # Changed from self.__width to self._width and self.__height to self._height

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:  # Changed from self.__width to self._width and self.__height to self._height
            return ""

        rect = []
        for i in range(self._height):  # Changed from self.__height to self._height
            [rect.append('#') for j in range(self._width)]  # Changed from self.__width to self._width
            if i != self._height - 1:  # Changed from self.__height to self._height
                rect.append("\n")
        return "".join(rect)

