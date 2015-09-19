#!/usr/bin/python
# Usage: python post_process.py source.dfxp output{.txt}

import tt2srt
import sys
import os
import cPickle as pickle

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
# lines_to_remove = []
sentences = []

### The code below deletes timestamps and empty lines
# for line in text:
#     if (is_number(line[0]) or (line[0] == '\n')):
#         lines_to_remove.append(line);

# for line in lines_to_remove:
#     text.remove(line)

### The code below creates an array of packets containing
### the timestamp and all the lines below it in the SRT file.
take = False
tmp = ""
for line in text:
    if(take):
        tmp = tmp + " " + line.rstrip('\n')
    if(line.find(":") > -1): # if a line contains a colon, it is a timestamp
        take = True
    if(line[0] == '\n'): # if it is an empty line, it's the end of the sentence
        take = False
        sentences.append(tmp)
        tmp = ""

pickle.dump( sentences, open( "speech.p", "wb" ) )
print sentences[0:30]
# print text[0:30]

srt_file.close()
# os.remove(temp_dest)
