import nltk
from nltk.corpus import PlaintextCorpusReader
#import nltk
#nltk.download('punkt')


corpus_root = 'C:\\Users\\Rawool\\Downloads\\NLP'

try:
    filelist = PlaintextCorpusReader(corpus_root, '.*', encoding='latin1')
except FileNotFoundError:
    print("Error: Corpus directory not found. Please check the path:", corpus_root)
    exit()

# Print the list of file identifiers (IDs) for the text files found in the directory
print('\nFile list:\n')
print(filelist.fileids())
print(filelist.root)

# Analyze statistics for each text
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')

for fileid in filelist.fileids():
    try:
        num_chars = len(filelist.raw(fileid))
        num_words = len(filelist.words(fileid))
        num_sents = len(filelist.sents(fileid))
        num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
        
        # Compute statistics and print them for each text file
        print(int(num_chars / num_words), '\t\t\t', int(num_words / num_sents), '\t\t\t',
              int(num_words / num_vocab), '\t\t', fileid)
    except ZeroDivisionError:
        print("Error: Division by zero occurred while computing statistics for file:", fileid)
