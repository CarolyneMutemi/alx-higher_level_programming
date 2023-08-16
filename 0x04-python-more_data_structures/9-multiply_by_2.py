#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    if a_dictionary is None:
        return None
    new = a_dictionary.copy()
    for k, v in new.items():
        new[k] = v * 2
    return new
