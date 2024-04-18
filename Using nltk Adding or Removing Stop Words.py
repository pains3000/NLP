import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords dataset if not already downloaded
nltk.download('stopwords')

# Define the input text
text = "Yashesh likes to play football, however he is not too fond of tennis."

# Tokenize the input text into words
text_tokens = word_tokenize(text)

# Remove stopwords from the tokenized text using NLTK's stopwords corpus
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

# Print the tokens without stopwords
print(tokens_without_sw)

# Add the word 'play' to the NLTK stop word collection
all_stopwords = stopwords.words('english')
all_stopwords.append('play')

# Remove stopwords again with the updated stop word collection
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

# Remove the word 'not' from the stop word collection
all_stopwords.remove('not')

# Remove stopwords again with the updated stop word collection
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
