import spacy

# Load the English model for Spacy
nlp = spacy.blank("en")

# Create a string input
str_input = "I love to study Natural Language Processing in Python"

# Create an instance of document; doc object is a container for a sequence of Token objects
doc = nlp(str_input)

# Read the words; Print the words
words = [word.text for word in doc]
print(words)
