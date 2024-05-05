# libs
import random
import json
import pickle

import numpy as np
import tensorflow as tf
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


# intents dictionary
intents = json.loads(open('./intents/intents.json').read())

# ignored characters
# words -> list of tokenized words
# tags -> tags defined from dictionary
# wordTag -> word (tokenized) and tag relation
exclude = ['.', ',', '!', '?']
words = []
tags = []
wordTag = []

# iterates over the dictionary
for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        wordTag.append((tokens, intent['tag']))
        if intent['tag'] not in tags:
            tags.append(intent['tag'])

lem = WordNetLemmatizer()
words = [lem.lemmatize(word) for word in words if word not in exclude]  # if word is not in exclude, lemmatize word
#print("Unsorted: ", words)
words = sorted(set(words))  # removes duplicated words
#print("Sorted: ", words)
tags = sorted(set(tags))  # removes duplicate tags

# 
pickle.dump(words, open('./pkl/words.pkl', 'wb'))
pickle.dump(tags, open('./pkl/tags.pkl', 'wb'))

