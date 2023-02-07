#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    n = len(argv)
    if (n - 1) == 0:
        print("{} arguments.".format(n - 1))
    elif (n - 1) == 1:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))

    for i in range(1, n):
        print("{}: {}".format(i, str(argv[i])))
