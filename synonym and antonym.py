import nltk
from nltk.corpus import wordnet

# Print synsets for the word "active"
print(wordnet.synsets("active"))

# Print antonyms of the word "active"
print(wordnet.lemma('active.a.01.active').antonyms())

# Compare path similarity between synsets of "football" and "soccer"
syn1 = wordnet.synsets('football')
syn2 = wordnet.synsets('soccer')

# Loop through each synset of "football" and "soccer" and calculate path similarity
for s1 in syn1:
    for s2 in syn2:
        print("Path similarity of:")
        print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
        print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
        print(" is", s1.path_similarity(s2))
        print()
