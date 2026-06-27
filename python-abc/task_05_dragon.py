#!/usr/bin/env python3
"""Dragon module."""


class SwimMixin:
    """Mixin that adds swimming."""

    def swim(self):
        """Swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying."""

    def fly(self):
        """Fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""

    def roar(self):
        """Roar."""
        print("The dragon roars!")
