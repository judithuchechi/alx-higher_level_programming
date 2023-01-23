#!/usr/bin/python3

def uppercase(str):
    for i in str:
        i = ord(i)
        if i <= 122 and i >= 97:
            i = chr(i - 32)
        else:
            i = chr(i)
        print("{}".format(i), end='')
    print()
