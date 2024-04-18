import nltk
nltk.download('treebank')

from nltk.corpus import treebank_chunk

# Print the tagged sentence
print(treebank_chunk.tagged_sents()[0])

# Print the chunked sentence
print(treebank_chunk.chunked_sents()[0])

# Draw the parse tree of the chunked sentence
treebank_chunk.chunked_sents()[0].draw()
