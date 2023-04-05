import json
import random
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

# These nltk libs are sentence tokenizers that will aid the lemmatizer
nltk.download('punkt')
nltk.download('wordnet')

# Lemmatizer helps reduce words to their root
# Example: work = working worked works
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

# Serialize data into files
pickle.dump(words, open('words.pk1', 'wb'))
pickle.dump(words, open('classes.pk1', 'wb'))

# Using bag of words method for pattern match
# Bag of words: set the individual values to eithrer 0 or 1 if it occurs in that pattern
training = []
empty_output = [0] * len(classes)

for combo in combos:
    word_bag = []
    word_patterns = combo[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        word_bag.append(1) if word in word_patterns else word_bag.append(0)

    output_row = list(empty_output)
    output_row[classes.index((combo[1]))] = 1
    training.append([word_bag, output_row])

random.shuffle(training)
training = np.array(training)

# Features and labels for supervised training of neural-net 
# Labels are the prediction or forecasts
# Features are descriptive attributes 
train_x = list(training[:,0]) # Features
train_y = list(training[:,1]) # Labels

# Building neural-net model 
# relu = rectified linear unit
# Sequential model orders and sequences i/o
# softmax = converts vector of numbers to vector of probabilities
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu')) 
model.add(Dropout(0.5)) # prevents overfitting
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5)) # prevents overfitting
model.add(Dense(len(train_y[0]), activation='softmax')) 

# SGD: Stochastic Gradient Descent is an algo used to optimize i/o matches 
sgd = SGD(learning_rate=0.01,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd, metrics=['accuracy'])

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose='1')
model.save("miniGPT_model.model")
print("done")
