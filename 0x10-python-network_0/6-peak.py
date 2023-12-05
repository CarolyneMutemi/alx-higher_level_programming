#!/usr/bin/python3
"""
Has the find_peak function.
"""

def find_peak(lis):
    """
    Finds a peak in a list of unsorted integers.
    Args:
        list - unsorted list being checked.
    Return:
        an integer that is the peak of the list.
    """
    if len(lis) == 0:
        return None
    mid = len(lis) // 2
    l = mid - 1
    r = mid + 1
    while l >= 0 and r <= len(lis) - 1:
        if lis[mid] > lis[l] and lis[mid] > lis[r]:
            return lis[mid]
        if lis[l] >= lis[mid] and lis[mid] > lis[r]:
            mid = l
        else:
            mid = r
        l = mid - 1
        r = mid + 1
    return lis[mid]
