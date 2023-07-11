#!/usr/bin/python3
"""Defines a function for converting a Python class to JSON."""


def class_to_json(obj):
    """Return the dictionary representation of a Python class.

    Args:
        obj (object): The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
