#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize new square.

        Args:
            size: Size ofa side of new square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the current size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square.

        Returns:
           The size of the new square.
        """
        return (self.__size ** 2)
