#!/usr/bin/python3
"""State a Python class-to-JSON function."""


def class_to_json(obj):
    """Takes back the dictionary represntation of a simple data structure."""
    return obj.__dict__
