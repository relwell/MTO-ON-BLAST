import pickle, os, argparse, nltk, re, random

### defines -- perl has changed me forever ###

def prep(sent):
    return re.sub(r" ([!\.:'\"\)\(;,?])", r"\1", sent).replace('( ', '(').replace(' * ', '*')

##############################################

parser = argparse.ArgumentParser(description='Build a language model or use an existing one. You should run mto-analyze.py first.')
parser.add_argument('-p', dest='pickle', action='store', type=str, help='Pickle file (default: ./sentences.raw)', default='./sentences.raw')
parser.add_argument('-s', dest='num_sentences', action='store', type=int, default=100, help='Number of sentences')
parser.add_argument('-n', dest='ngram_order', action='store', type=int, default=3, help="N-Gram model order")

args = parser.parse_args()


data = pickle.load(open(args.pickle))
text = nltk.Text(data)
estimator = lambda fdist, bins: nltk.LidstoneProbDist(fdist, 0.2) 
ngram_model = nltk.model.NgramModel(3, text, estimator) 

print "\n".join([prep(sent) for sent in  \
                     [' '.join(ngram_model.generate(random.randrange(5,25))) for i in range(0,args.num_sentences)] \
                 if sent.count(' ') > 5])


