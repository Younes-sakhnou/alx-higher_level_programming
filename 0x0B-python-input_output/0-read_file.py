#!/usr/bin/python3
"""Text file-reading function."""


def read_file(filename=""):
    """this function reads texts file and prints it to the stdout."""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
