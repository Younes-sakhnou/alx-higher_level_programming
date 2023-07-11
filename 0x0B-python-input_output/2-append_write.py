#!/usr/bin/python3
"""Defines a function for appending content to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of the specified text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The content to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)