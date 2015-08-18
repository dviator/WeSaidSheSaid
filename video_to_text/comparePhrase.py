import cPickle as pickle


def findCompletePhrase(phrase1, phrase2):
	if phrase1 in phrase2:
		return phrase2
	else:
		return phrase1, phrase2



print findCompletePhrase("Americans", "All Americans")
print findCompletePhrase("All Americans", "All Americans are")
print findCompletePhrase("All Americans are", "really really beautiful")
