#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, r_width, r_height):
        """Intialize a new Rectangle.

        Args:
            r_width (int): The width of the new Rectangle.
            r_height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", r_width)
        self.__width = r_width
        super().integer_validator("height", r_height)
        self.__height = r_height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
