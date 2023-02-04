#!/usr/bin/python3

def remove_char_at(str, n):

    new = ""
    strlen = len(str)
    j = 0

    for w in str:
        if j < strlen:
            if j != n:
                new = new + (w)
            j = j + 1
    return (new)
