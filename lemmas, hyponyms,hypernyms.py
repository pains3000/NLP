import nltk
from nltk.corpus import wordnet

print(wordnet.synsets("computer"))
print(wordnet.synset("computer.n.01").lemma_names())

# Print all lemmas for each synset of "computer"
for synset in wordnet.synsets("computer"):
    print(f'{synset} --> {synset.lemma_names()}')

print(wordnet.synset('computer.n.01').lemmas())
print(wordnet.lemma('computer.n.01.computing_device').synset())
print(wordnet.lemma('computer.n.01.computing_device').name())

# Get the list of hyponyms (more specific concepts) of the synset "computer.n.01"
syn = wordnet.synset('computer.n.01')
print(syn.hyponyms)
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])

# Semantic similarity between "car" and "vehicle"
vehicle = wordnet.synset('vehicle.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))
