import spacy
import nltk
from nltk.tokenize import word_tokenize

# Download the English model for Spacy
!python -m spacy download en

# Load the English model for Spacy
sp = spacy.load('en_core_web_sm')

# Get the default stop words from Spacy
all_stopwords = sp.Defaults.stop_words

# Add the word "play" to the stop word collection
all_stopwords.add("play")

# Define the input text
text = "Yashesh likes to play football, however he is not too fond of tennis."

# Tokenize the input text into words
text_tokens = word_tokenize(text)

# Remove stopwords from the tokenized text using Spacy's stop word collection
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

# Remove 'not' from the stop word collection
all_stopwords.remove('not')

# Remove stopwords again with the updated stop word collection
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
