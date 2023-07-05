#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of .?:

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1
    separators = ['.', '?', ':']

    while char < len(text):
        print(text[char], end='')
        if text[char] == "\n" or text[char] in separators:
            if text[char] in separators:
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
