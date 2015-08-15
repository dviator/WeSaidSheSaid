#!/usr/bin/python

import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

filename = sys.argv[1]

f = open(filename, "r")
lines = f.readlines()
f.close()

f = open(filename, "w")
for line in lines:
  	if not is_number(line[0]):
    	f.write(line)
f.close()