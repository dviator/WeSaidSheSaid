import cPickle as pickle


def findCompletePhrase(phrase1, phrase2):
	if phrase1 in phrase2:
		return phrase2, None
	else:
		return phrase1, phrase2

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
cleanSpeech = []
for p in speech:
	cleanSpeech.append(p)
	if len(cleanSpeech) >= 2:
		phrase2 = cleanSpeech.pop().split()
		phrase1 = cleanSpeech.pop().split()
		print phrase1, phrase2
	#Not working yet
	for x in phrase2:
		if x not in phrase1:
			cleanSpeech.append(x)

print cleanSpeech


#print speech



#print findCompletePhrase("Americans", "All Americans")
#print findCompletePhrase("All Americans", "All Americans are")
#print findCompletePhrase("All Americans are", "really really beautiful")

