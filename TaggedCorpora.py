import nltk
from nltk import tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('words')

# Input paragraph
para = "Hello! My name is Gangaram Rawool. Today you'll be learning NLTK."

# Perform sentence tokenization
sents = tokenize.sent_tokenize(para)
print("\nSentence Tokenization\n===================")
print(sents)

# Perform word tokenization
print("\nWord Tokenization\n===================")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
