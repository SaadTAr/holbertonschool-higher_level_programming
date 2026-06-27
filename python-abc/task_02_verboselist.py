#!/usr/bin/env python3
"""VerboseList module."""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Append an item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a message."""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove an item and print a message."""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Pop an item and print a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
