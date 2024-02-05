#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted outputing for the built-in list class."""

    def print_sorted(self):
        """Output a list in sorted ascending order."""
        print(sorted(self))
