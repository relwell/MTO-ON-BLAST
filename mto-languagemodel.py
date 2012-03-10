import pickle, os, argparse, nltk, re, random

parser = argparse.ArgumentParser(description='Build a language model or use an existing one. You should run mto-analyze.py first.')
parser.add_argument('-c', dest='create', action='store_true', help='Create new language model, even if one exists')
parser.add_argument('-p', dest='pickle', action='store', type=str, help='Pickle file (default: ./sentences.raw)', default='./sentences.raw')
parser.add_argument('-n', dest='num_sentences', action='store', type=int, default=100, help='Number of sentences')

args = parser.parse_args()

data = pickle.load(open(args.pickle))

if args.create:
    text = nltk.Text(data)
    pickle.dump(text, open('languagemodel.prepped', 'w'))
else:
    text = pickle.load(open('languagemodel.prepped'))


for i in range(0,args.num_sentences):
    text.generate(random.randrange(5, 20))


