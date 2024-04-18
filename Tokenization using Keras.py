from keras.preprocessing.text import text_to_word_sequence

# Create a string input
str_input = "I love to study Natural Language Processing in Python"

# Tokenizing the text
tokens = text_to_word_sequence(str_input)
print(tokens)
