#!/usr/bin/python3
class Sqaure:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method to iinitialize the sqaure object
        """
        if not is isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an in integer")
        else:
            self.__size = int(size)
