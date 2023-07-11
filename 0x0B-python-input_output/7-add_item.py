#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load existing items from the JSON file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        items = []

    # Extend the items list with the command-line arguments
    items.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(items, "add_item.json")
