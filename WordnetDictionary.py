import nltk
from nltk.corpus import wordnet
#import nltk
#nltk.download('wordnet')


# Print all synsets for the word "computer"
print(wordnet.synsets("computer"))

# Print definition of the word "computer"
print(wordnet.synset("computer.n.01").definition())

# Print examples of usage for the word "computer"
print("Examples:", wordnet.synset("computer.n.01").examples())

# Print antonyms of the word "buy"
print(wordnet.lemma('buy.v.01.buy').antonyms())
