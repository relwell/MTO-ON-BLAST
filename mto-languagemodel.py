import pickle, os, argparse, nltk, re, random

parser = argparse.ArgumentParser(description='Build a language model or use an existing one. You should run mto-analyze.py first.')
parser.add_argument('-p', dest='pickle', action='store', type=str, help='Pickle file (default: ./sentences.raw)', default='./sentences.raw')
parser.add_argument('-s', dest='num_sentences', action='store', type=int, default=100, help='Number of sentences')
parser.add_argument('-n', dest='ngram_order', action='store', type=int, default=3, help="N-Gram model order")

args = parser.parse_args()

"""
We're using this to clean up some of the whitespace and punctuation issues.
"""
def prep(sent):
    return re.sub(r" ([!\.:'\"\)\(;,?])", r"\1", sent).replace('( ', '(').replace(' * ', '*')

""" load the pickled raw sentence data from mto-analyze """
data = pickle.load(open(args.pickle))

""" ingest this data with nltk.text """
text = nltk.Text(data)

"""
this estimator is used to help smooth ngram probabilities,
helping to introduce novel (unseen) events into our model
"""
estimator = lambda fdist, bins: nltk.LidstoneProbDist(fdist, 0.2) 
"""
This NgramModel is responsible for generating text for us
"""
ngram_model = nltk.model.NgramModel(args.ngram_order, text, estimator=estimator) 

"""
Send the number of sentences requested, of random length between 5 and 25 words, to stdout
"""
print "\n".join([prep(sent) for sent in  \
                     [' '.join(ngram_model.generate(random.randrange(5,25))) for i in range(0,args.num_sentences)] \
                 if sent.count(' ') > 5])


