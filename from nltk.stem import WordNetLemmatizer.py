from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print("word :\tlemma")
print("rocks:", lemmatizer.lemmatize("rocks"))
print("corpora:", lemmatizer.lemmatize("corpora"))
# 'better' is an adjective, so we specify the POS tag as 'a'
print("better:", lemmatizer.lemmatize("better", pos="a"))
