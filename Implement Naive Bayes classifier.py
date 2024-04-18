import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Load data
sms_data = pd.read_csv("spam.csv", encoding='latin-1')

# Text preprocessing
stemming = PorterStemmer()
corpus = []
for i in range(len(sms_data)):
    s1 = re.sub('[^a-zA-Z]', repl=' ', string=sms_data['v2'][i]).lower().split()
    s1 = [stemming.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    s1 = ' '.join(s1)
    corpus.append(s1)

# Feature extraction
countvectorizer = CountVectorizer()
x = countvectorizer.fit_transform(corpus).toarray()
y = sms_data['v1'].values

# Splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=2)

# Model training
multinomialnb = MultinomialNB()
multinomialnb.fit(x_train, y_train)

# Prediction
y_pred = multinomialnb.predict(x_test)

# Model evaluation
print(classification_report(y_test, y_pred))
print("accuracy_score:", accuracy_score(y_test, y_pred))
