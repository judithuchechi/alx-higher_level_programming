#!/usr/bin/python3

def islower(c):
	c = ord(c)
	if c >= 65 and c <= 90:
		return False
	elif c >= 97 and c <= 122:
		return True
