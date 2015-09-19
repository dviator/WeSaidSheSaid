#########################################################################
############## IMPORT STATEMENTS ########################################
#########################################################################
from __future__ import unicode_literals
from xml.dom.minidom import parse
import sys
import os
import operator
import youtube_dl

#########################################################################
############## CLASS DECLARATION ########################################
#########################################################################

class transcriber:
    """ Class Transcriber 
    -   Takes videos from CSPAN and translates the native dfxp into readable text
    -   Methods
        -   transcribe(url, name)
                - takes video from url and translates the dfxp into text
                - the output is saved into a file "${name}.txt"
                - intended to be called by the webCrawler module"""

    #Given a URL, uses YoutubeDL to download the subtitles of a speech in dfxp format. Call by passing a url and specify the path in which to store the file.             
    def DownloadSpeech(url,filename):
        class MyLogger(object):
            def debug(self, msg):
                print(msg)

            def warning(self, msg):
                print(msg)

            def error(self, msg):
                print(msg)


        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now converting ...')

        outputName = 'data/' + filename
        ydl_opts = {
            'logger': MyLogger(),
            'writesubtitles': True,
            'skip_download': True,
            'outtmpl': outputName
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


        # Member object 'speech' will hold the translated speech text
    speech = []

# end class transcriber

#########################################################################
############### TRANSLATE DFXP TO SRT ###################################
#########################################################################

# translate takes in a dfxp file and translates it to SRT

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

# truncateSRT will return the sentences variable.  This will replace the need for outputting to speech.p
# This function calls 'translate' and so 'source' must be dfxp formatted

def truncateSRT(source, name):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    temp_dest = name + '_tmp.srt'
    translate(source, temp_dest)

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

    srt_file.close()
    return sentences 

#end function truncateSRT

#########################################################################
############### CLEAN UP SPEECH #########################################
#########################################################################

# cleanUpSpeech implements the algorithm which takes SRT and translates it into readable text. 

def cleanUpSpeech(sentences):
    def findCompletePhrase(phrase1, phrase2):
        if phrase1 in phrase2:
            return phrase2, None
        else:
            return phrase1, phrase2

    ## get rid of incomplete duplicate phrases generated by cc
    ## keeps only the longest, most complete version of each phrase
    rawSRT = sentences
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

# end function cleanUpSpeech

#########################################################################
############### MAIN ####################################################
#########################################################################

sentences = truncateSRT("hillary_clinton_1.en.dfxp", "hillary_clinton_1")
cleanUpSpeech(sentences)
