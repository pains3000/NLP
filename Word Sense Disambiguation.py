from nltk.corpus import wordnet as wn

def get_first_sense(word, pos=None):
    if pos:
        synsets = wn.synsets(word, pos)
    else:
        synsets = wn.synsets(word)
    return synsets[0] if synsets else None

best_synset = get_first_sense('bank')
if best_synset:
    print ('%s: %s' % (best_synset.name(), best_synset.definition()))

best_synset = get_first_sense('set','n')
if best_synset:
    print ('%s: %s' % (best_synset.name(), best_synset.definition()))

best_synset = get_first_sense('set','v')
if best_synset:
    print ('%s: %s' % (best_synset.name(), best_synset.definition()))
