from nltk.tag import UnigramTagger
from nltk.corpus import treebank

# Training using first 10 tagged sentences of the treebank corpus as data.
train_sents = treebank.tagged_sents()[:10]

# Initializing UnigramTagger
tagger = UnigramTagger(train_sents)

# Print the first sentence of the treebank corpus as a list
print("First Sentence:", treebank.sents()[0])

# Tag the first sentence using the UnigramTagger
print("Tagged First Sentence:", tagger.tag(treebank.sents()[0]))

# Finding the tagged results after training
tagged_result = tagger.tag(treebank.sents()[0])
print("Tagged Result after Training:", tagged_result)

# Overriding the context model
tagger = UnigramTagger(model={'Pierre': 'NN'})
print("Tagged Result with Overridden Context Model:", tagger.tag(treebank.sents()[0]))
