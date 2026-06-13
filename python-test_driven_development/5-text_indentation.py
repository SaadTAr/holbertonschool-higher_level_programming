#!/usr/bin/python3
"""Text indentation module."""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
