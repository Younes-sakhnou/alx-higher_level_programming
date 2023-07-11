# Defines a function for writing content to a text file.

def write_file(filename="", content=""):
    """
    Write content to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(content)
