#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size):
        """Constractor new square.

        Args:
            size: Size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the size of the new square.

        Raises:
          TypeError: If the size is not an integer.
          ValueError: If the size is less than 0.
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
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
