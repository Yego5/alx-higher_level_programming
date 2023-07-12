#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, val):
        """Override == operator with != behavior."""
        return super().__ne__(val)

    def __ne__(self, val):
        """Override != operator with == behavior."""
        return super().__eq__(val)
