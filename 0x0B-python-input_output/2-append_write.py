#!/usr/bin/python3
"""file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of file.

    Args:
        filename (str): name of the file to append to.
        text (str): string to append to the file.
    Returns:
        number of appended letters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
