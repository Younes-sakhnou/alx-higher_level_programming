#!/usr/bin/python3
"""Defines a function for reading a JSON file."""
import json


def load_from_json_file(filename):
    """Read a JSON file and return a Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
