#!/usr/bin/python3
"""Defines a function for converting a string to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (str): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
