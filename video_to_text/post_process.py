#!/usr/bin/python
# Usage: python post_process.py source.dfxp output{.txt}

import tt2srt
import sys
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

temp_dest = sys.argv[2] + '_tmp.srt'
tt2srt.translate(sys.argv[1], temp_dest)

srt_file = open(temp_dest, 'r')
text = srt_file.readlines()
lines_to_remove = []

for line in text:
    if (is_number(line[0]) or (line[0] == '\n')):
        lines_to_remove.append(line);

for line in lines_to_remove:
    text.remove(line)

print text[0:30]

srt_file.close()
# os.remove(temp_dest)