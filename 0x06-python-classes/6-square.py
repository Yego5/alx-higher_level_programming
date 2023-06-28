#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.s_size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.s_size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.s_position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.s_position = value

    def area(self):
        """Return the current area of the square."""
        return self.s_size * self.s_size

    def my_print(self):
        """Print the square with the # character."""
        if self.s_size == 0:
            print("")
            return

        for _ in range(self.s_position[1]):
            print("")

        for _ in range(self.s_size):
            print(" " * self.s_position[0], end="")
            print("#" * self.s_size)
