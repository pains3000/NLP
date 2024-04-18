import nltk
from nltk.corpus import brown
from nltk.tag import RegexpTagger

# Load the Brown Corpus and extract the first sentence from the 'news' category
test_sent = brown.sents(categories='news')[0]

# Define regular expression patterns for tagging
patterns = [
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),    # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'),    # articles
    (r'.*ness$', 'NN'),                 # nouns formed from adjectives
    (r'.*ly$', 'RB'),                   # adverbs
    (r'.*s$', 'NNS'),                   # plural nouns
    (r'.*ing$', 'VBG'),                 # gerunds
    (r'.*ed$', 'VBD'),                  # past tense verbs
    (r'.*', 'NN')                       # nouns (default)
]

# Create a RegexpTagger with the defined patterns
regexp_tagger = RegexpTagger(patterns)

# Print the RegexpTagger
print("RegexpTagger:", regexp_tagger)

# Tag the test sentence using the RegexpTagger
tagged_sent = regexp_tagger.tag(test_sent)

# Print the tagged sentence
print("Tagged Sentence:", tagged_sent)
