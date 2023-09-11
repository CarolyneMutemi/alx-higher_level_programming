#!/usr/bin/python3

"""
Defines the MyList function.
"""


class MyList(list):
    """
    MyList class - inherits from class.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        my = self.copy()
        my.sort()
        print(my)
