#!/usr/bin/python3
"""Defines a function for writing an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a JSON file.

    Args:
        my_obj (object): The object to be written to the JSON file.
        filename (str): The name of the file to save the JSON content to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
