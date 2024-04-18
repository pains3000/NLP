import spacy
from spacy import displacy

# Load spaCy model
sp = spacy.load('en_core_web_sm')

# POS tagging
sen = sp(u"I like to play football. I hated it in my childhood though")
print(sen.text)
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Finding the Number of POS Tags
num_pos = sen.count_by(spacy.attrs.POS)
for k, v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')

# Visualizing Parts of Speech Tags
displacy.serve(sen, style='dep', options={'distance': 120})
