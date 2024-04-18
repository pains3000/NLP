import nltk
from nltk.stem import PorterStemmer

word_stemmer = PorterStemmer()
print(word_stemmer.stem('writing'))
