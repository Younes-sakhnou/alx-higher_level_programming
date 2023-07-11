#!/usr/bin/python3
"""Defines a function for converting JSON to a Python object."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
