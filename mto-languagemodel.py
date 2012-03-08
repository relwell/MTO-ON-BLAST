from nltk.model import ngram
import pickle, os, argparse

parser = argparse.ArgumentParser(description='Build a language model or use an existing one.')
parser.add_argument('-c', dest='create', action='store_true', help='Create new language model, even if one exists')
parser.add_argument('-n', dest='ngram_order', action='store', type=int, help='N-Gram order')
parser.add_argument('-p', dest='pickle', action='store', type=str, help='Pickle file (default: ./unigrams.prepped)', default='./unigrams.prepped')

args = parser.parse_args()

unigramsprepped = pickle.load(open(args.pickle))

model = ngram.NgramModel(args.ngram_order, unigramsprepped)


for i in range(0, 100):
    model.generate(i+1 % 10)
