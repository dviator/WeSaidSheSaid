# Usage: python transcriber.py source.dfxp output{.txt}


#########################################################################
############### TRANSLATE DFXP TO SRT ###################################
#########################################################################

from xml.dom.minidom import parse
import sys

def translate(source, output):
    i=1
    # dom = parse(sys.argv[1])
    # out = open(sys.argv[], 'w')
    dom = parse(source)
    out = open(output, 'w')
    body = dom.getElementsByTagName("body")[0]
    paras = body.getElementsByTagName("p")
    for para in paras:
        out.write(str(i) + "\n")
        try:
            a=float(para.attributes['begin'].value)
        except ValueError:
            a=0
        out.write('%02d' %(int(a/3600)))
        out.write(":")
        out.write('%02d' % (int(a/60)-60*(int(a/3600))))
        out.write(':')
        out.write('%02d' % (a%60))
        out.write(',')
        out.write('%03d' % (a%60.0-a%60))
        out.write(' --> ')

        a= float(para.attributes['end'].value)

        out.write('%02d' %(int(a/3600)))
        out.write(":")
        out.write('%02d' % (int(a/60)-60*(int(a/3600))))
        out.write(':')
        out.write('%02d' % (a%60))
        out.write(',')
        out.write('%03d' % (a%60.0-a%60))

        out.write("\n")
        for child in para.childNodes:
            if child.nodeName == 'br':
                out.write("\n")
            elif child.nodeName == '#text':
                out.write(unicode(child.data).encode('utf=8'))
        out.write("\n\n")
        i += 1
# end function 'translate'

#########################################################################
############### TRUNCATE SRT ############################################
#########################################################################

import os
import cPickle as pickle

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

temp_dest = sys.argv[2] + '_tmp.srt'
translate(sys.argv[1], temp_dest)

srt_file = open(temp_dest, 'r')
text = srt_file.readlines()
sentences = []

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
# print sentences[0:30]

srt_file.close()

#########################################################################
############### CLEAN UP SPEECH #########################################
#########################################################################

import operator


def findCompletePhrase(phrase1, phrase2):
    if phrase1 in phrase2:
        return phrase2, None
    else:
        return phrase1, phrase2

## get rid of incomplete duplicate phrases generated by cc
## keeps only the longest, most complete version of each phrase
rawSRT = pickle.load( open("speech.p","r"))
speech = []
for p in rawSRT:
    speech.append(p)
    if len(speech) >= 2:
        phrase2 = speech.pop()
        phrase1 = speech.pop()
        fullPhrase, lastPhrase= findCompletePhrase(phrase1, phrase2)
        if lastPhrase is not None:
            speech.append(fullPhrase)
            speech.append(lastPhrase)
        else:
            speech.append(fullPhrase)
                #print phrase2
        #print phrase1
    else: 
        pass

### Make the composite phrase into the new "1st phrase" of the next comparison

sub_speech = speech[0: len(speech)]
clean_speech = []
iter_count = 0

sub_speech.reverse()

for phrase in sub_speech:
    if ((phrase != ' ') and (phrase != '')):
        clean_speech.append(phrase)
        iter_count += 1
    if ( len(clean_speech) == 2):
        phraseA = clean_speech.pop().split()
        # print "Phrase A: ", phraseA
        phraseB = clean_speech.pop().split()
        # print "Phrase B: ", phraseB
        composite_phrase = []

        #iron clad error checking
        matchIndex = []
        searchSegment = []
        if (len(phraseB) >= 1) and (len(phraseA) >= 1):
            searchSegment = phraseA[-len(phraseB)::]
            for i, token in enumerate(searchSegment):
                if token == phraseB[0]:
                    matchIndex.append(i)
            if len(matchIndex) == 0:
                composite_phrase = phraseA + phraseB
            if len(matchIndex) == 1:
                composite_phrase = phraseA[0:-len(phraseB)] + searchSegment[0:matchIndex[0]] + phraseB
            elif len(matchIndex) > 1:
                IndexMatchCounter = dict.fromkeys(matchIndex, 0)
                for i in matchIndex:
                    postMatchSegment = searchSegment[i:]
                    for j, token in enumerate(searchSegment[i:]):
                        if token == phraseB[j]:
                            IndexMatchCounter[i] += 1               
                trueIndex = max(IndexMatchCounter.iteritems(), key=operator.itemgetter(1))[0]
                composite_phrase = phraseA[0:-len(phraseB)] + searchSegment[0:trueIndex] + phraseB
            clean_speech.append(" ".join(composite_phrase))

print clean_speech