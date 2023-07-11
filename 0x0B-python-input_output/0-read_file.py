#!/usr/bin/python3

def read_file(filename=""):
    """this function reads texts file and prints it to the stdout."""


with open("my_file_0.txt", encoding="utf-8") as myFile:
    print(myFile.read(), end="")
