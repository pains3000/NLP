import nltk
from nltk.tag import DefaultTagger
#import nltk
#nltk.download('treebank')


# Create a DefaultTagger with the tag 'NN' (noun)
exptagger = DefaultTagger('NN')

# Import the treebank corpus and get tagged sentences for testing
from nltk.corpus import treebank
testsentences = treebank.tagged_sents()[1000:]  # Using tagged sentences starting from index 1000

# Evaluate the performance of the DefaultTagger on the test sentences
gold_standard = [[(word, tag) for word, tag in sent] for sent in testsentences]
accuracy = exptagger.evaluate(gold_standard)
print("Accuracy:", accuracy)

# Tagging a list of sentences
# Define the list of sentences
sentences = [['Hi', ','], ['How', 'are', 'you', '?']]

# Tag the list of sentences using the DefaultTagger
tagged_sentences = exptagger.tag_sents(sentences)
print("Tagged Sentences:", tagged_sentences)
