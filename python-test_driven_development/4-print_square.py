#!/usr/bin/python3
"""Module that prints a square."""


def print_square(size):
    """Print a square with the character #."""

    if type(size) is float and size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    for i in range(size):
        print("#" * size)
