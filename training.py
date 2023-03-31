import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# punkt is sentence tokenizer that will aid the lemmatizer
nltk.download('punkt')
nltk.download('wordnet')

# Lemmatizer helps reduce words to their root. example: work = working worked works
lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
combos = []
classes = []
ignore_letters = [',','.','!','?']

# Split sentence into individual words
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        combos.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words = [lemmatizer.lemmatize(word)
    for word in words if word not in ignore_letters]

words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pk1', 'wb'))
pickle.dump(words, open('classes.pk1', 'wb'))

print(words)
