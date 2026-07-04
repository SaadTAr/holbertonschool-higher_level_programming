#!/usr/bin/python3
"""Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation."""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes from dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
