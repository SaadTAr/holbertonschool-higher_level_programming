#!/usr/bin/python3
"""Square module."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize square."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return string representation."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
