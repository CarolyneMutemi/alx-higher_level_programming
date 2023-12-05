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
    left = mid - 1
    right = mid + 1
    # check for an instance where there is no peak
    # in the right side and switch to left
    check = 0
    while left >= 0 and right <= len(lis) - 1:
        if lis[mid] > lis[left] and lis[mid] > lis[right]:
            return lis[mid]
        if (lis[left] >= lis[mid] and lis[mid] > lis[right]) or check:
            mid = left
        else:
            mid = right
            if right == len(lis) - 1 and lis[len(lis) // 2] == lis[right]:
                mid = left
                check = 1
        left = mid - 1
        right = mid + 1
    return lis[mid]
