#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Takes back a list of an object's available attributes."""
    return (dir(obj))