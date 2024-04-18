import nltk
from collections import defaultdict
#import nltk
#nltk.download('averaged_perceptron_tagger')


# Tokenize the text and perform POS tagging
text = nltk.word_tokenize("Nick likes to play football. Nick does not like to play cricket.")
tagged = nltk.pos_tag(text)
print("Tagged words:", tagged)

# Extract noun words
noun_words = []
for word, pos_tag in tagged:
    if pos_tag.startswith('NN'):
        noun_words.append(word)
print("Noun words:", noun_words)

# Count the frequency of each noun word
word_freq = defaultdict(int)
for sub in noun_words:
    for word in sub.split():
        word_freq[word] += 1

# Find the word with maximum frequency
max_freq_word = max(word_freq, key=word_freq.get)

# Print the word with maximum frequency
print("Word with maximum frequency:", max_freq_word)
