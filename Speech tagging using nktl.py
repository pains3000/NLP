import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# Load training and sample text data
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# Train the Punkt tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# Tokenize the sample text using the trained tokenizer
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# Define a function to process content (perform POS tagging)
def process_content():
    try:
        for i in tokenized[:2]:  # Process first two sentences for demonstration
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

# Call the function to process content
process_content()
