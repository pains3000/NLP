import nltk
from nltk import CFG, ChartParser, Nonterminal, word_tokenize

# Define the grammar
grammar1 = CFG.fromstring("""
    S -> VP
    VP -> VP NP
    NP -> Det Noun
    Det -> 'that'
    Noun -> 'flight'
    VP -> 'Book'
""")

# Define the sentence
sentence = "Book that flight"

# Tokenize the sentence
all_tokens = word_tokenize(sentence)

# Create a chart parser
parser = ChartParser(grammar1)

# Parse the sentence and display parse trees
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
