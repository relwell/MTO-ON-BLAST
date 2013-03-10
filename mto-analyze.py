from nltk import tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pickle, sys

# was using headlinesPrepped.txt
file = open(sys.argv[1]) 

sentences = []

"""
Stopwords are function words that are the most
common and least meaningful words in English.
These include 'the', 'a', 'so', 'of', etc.
"""
englishStopWords = stopwords.words('English')
def good(token):
    global englishStopWords
    return token.isalnum() and token not in englishStopWords

print 'prepping...'
"""
Tokenize sentences from headlines. If the 
tokenized 'sentence' is one word long, append it
to the previous sentence.
"""
for line in file:
    tokenized = tokenize.sent_tokenize(line[:-1])
    for i in range(0,len(tokenized)):
        if len(tokenized[i]) == 1:
            sentences[-1] += tokenized[i]
        else:
            sentences.append(tokenized[i].lower())


"""
Tokenize the words all sentences into a single list
"""
allTokens = []
pw = tokenize.punkt.PunktWordTokenizer()
for sent in sentences:
    allTokens += pw.tokenize(sent)

"""
Strip out stopwords so we can do some statistical analysis
Note that it's pretty easy to make n-gram lists of varying 
order with list comprehensions.
"""
print 'prepping data...'
trigramsPrepped = ["%s %s %s" % (allTokens[i], allTokens[i+1], allTokens[i+2]) for i in range(0,len(allTokens)-2) if (good(allTokens[i]) and good(allTokens[i+1]))]
bigramsPrepped = ["%s %s" % (allTokens[i], allTokens[i+1]) for i in range(0,len(allTokens)-1) if good(allTokens[i]) ]
unigramsPrepped = [token for token in allTokens if good(token)]

"""
We use these frequency distributions 
to do some analysis on our corpus.
"""
print 'getting frequencies...'
trigramFreqs = FreqDist(trigramsPrepped)
bigramFreqs = FreqDist(bigramsPrepped)
unigramFreqs = FreqDist(unigramsPrepped)

"""
Print out statistics about our corpus
This looks better if you pipe it out to column -t
"""
print "||\tuni\t||\tbi\t.\t||\ttri"
univals = unigramFreqs.items()
bivals = bigramFreqs.items()
trivals = trigramFreqs.items()
for i in range(0,100):
    print "%3d\t%s\t||\t%s\t||\t%s" % (i, univals[i][0], bivals[i][0], trivals[i][0])

"""
We use these pickled values when generating text in mto-languagemodel.py
"""
print "\nSaving data..."
pickle.dump(unigramsPrepped, open('unigrams.prepped', 'w'))
pickle.dump(bigramsPrepped, open('bigrams.prepped', 'w'))
pickle.dump(trigramsPrepped, open('trigrams.prepped', 'w'))
pickle.dump(allTokens, open('unigrams.raw', 'w'))
pickle.dump(allTokens, open('sentences.raw', 'w'))

print "done"
