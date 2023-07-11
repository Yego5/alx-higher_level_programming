#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, sq_size):
        """Initialize a new square.

        Args:
            sq_size (int): The size of the new square.
        """
        self.integer_validator("size", sq_size)
        super().__init__(sq_size, sq_size)
        self.__size = sq_size
