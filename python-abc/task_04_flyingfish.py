#!/usr/bin/env python3
"""FlyingFish module."""


class Fish:
    """Fish class."""

    def swim(self):
        """Swim."""
        print("The fish is swimming")

    def habitat(self):
        """Habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Fly."""
        print("The bird is flying")

    def habitat(self):
        """Habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class."""

    def swim(self):
        """Swim."""
        print("The flying fish is swimming!")

    def fly(self):
        """Fly."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Habitat."""
        print("The flying fish lives both in water and the sky!")
