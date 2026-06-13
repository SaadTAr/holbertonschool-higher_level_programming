#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Add two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a == float("inf") or a == float("-inf"):
        raise OverflowError("cannot convert float infinity to integer")

    if b == float("inf") or b == float("-inf"):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
