from __future__ import division
import nltk, pprint, re
from nltk import word_tokenize

# How to import speech text from the root directory
import os
import sys
root = os.environ['WSSS_ROOT']
spath = os.path.join(root, root + '/wesaidshesaid/speeches/')
sys.path.insert(0,spath)

# Get a speech to play with
filename = "Huckabee_Campaign_Event.txt"
f = open(spath + filename, 'r')
raw = f.read()
print raw.rfind("REPUBLICAN")
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
print text.collocations()
f.close()