#!/usr/bin/python3
"""Module that defines MyList"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
