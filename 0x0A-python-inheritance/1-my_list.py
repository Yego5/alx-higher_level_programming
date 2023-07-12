#!/usr/bin/python3
"""Defines an inherited list class lst."""


class lst(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(slf):
        """Print a list in sorted ascending order."""
        print(sorted(slf))

