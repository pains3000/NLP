import nltk
from nltk import tokenize
from nltk import pos_tag, ne_chunk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

para = "Hello! My name is Beena Kapadia. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n", sents)

# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)

# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(pos_tag(words))
print("\nPOS Tagging\n===========\n", tagged_words)

# Chunking
tree = []
for index in range(len(sents)):
    tree.append(ne_chunk(tagged_words[index]))
print("\nchunking\n========\n")
print(tree)
