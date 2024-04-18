import nltk
from nltk.corpus import brown, inaugural, udhr

# Creating Conditional Frequency Distributions from Brown Corpus
fd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

# Creating Conditional Frequency Distributions for Specific Genres
genre_word = [
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
]

# Printing Information about the Genre-Word Pairs
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])

# Creating Conditional Frequency Distributions from Inaugural Address Corpus
cfd_inaugural = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

# Creating Conditional Frequency Distributions from Universal Declaration of Human Rights Corpus
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd_udhr = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)

# Tabulating Conditional Frequency Distributions for English and German
cfd_udhr.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)
