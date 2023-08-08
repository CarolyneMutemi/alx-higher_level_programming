#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    if n < len(str) and n > 0:
        for i in str:
            if str[n] == i:
                continue
            copy += i
    else:
        return str
    return copy
