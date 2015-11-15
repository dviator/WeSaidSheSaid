from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist

corpus_root = "/home/maevyn/Documents/WeSaidSheSaid/wesaidshesaid/speeches"
wordLists = PlaintextCorpusReader(corpus_root,'.*\.txt')

print wordLists.fileids()

fdist = FreqDist(wordLists.words())

print fdist.most_common(50)

fdist.plot(50, cumulative=True)

print wordLists.parsed_sents()