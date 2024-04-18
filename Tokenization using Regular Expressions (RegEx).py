import nltk
from nltk.tokenize import RegexpTokenizer

# Create a reference variable for Class RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps=True)

# Create a string input
str_input = "I love to study Natural Language Processing in Python"

# Use tokenize method
tokens = tk.tokenize(str_input)
print(tokens)
