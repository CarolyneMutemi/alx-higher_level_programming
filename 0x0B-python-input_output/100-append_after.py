#!/usr/bin/python3

"""
Has the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, \
        after each line containing a specific string
    Args:
        filename - the filename to look into.
        search_string - the string to match.
        new_string - The string to be appended after the line.
    """
    if isinstance(filename, str) and isinstance(search_string, str) \
            and isinstance(new_string, str):
        with open(filename, 'r', encoding='utf-8') as file:
            lis = file.readlines()
            for line in lis:
                if search_string in line:
                    lis = lis[:lis.index(line) + 1] + [new_string] \
                        + lis[lis.index(line)+1:]
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lis)
