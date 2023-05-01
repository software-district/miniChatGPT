import json
import random
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

# These nltk libs are sentence tokenizers that will aid the lemmatizer
nltk.download('popular')

# Lemmatizer helps reduce words to their root
# Example: work = working worked works
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

SGD = tf.keras.optimizers.legacy.SGD   # legacy runs faster on m1/m2 chips
Dense = tf.keras.layers.Dense
Dropout = tf.keras.layers.Dropout
Sequential = tf.keras.models.Sequential

words: list = []
combos: list = []
classes: list = []
ignore_letters: list = [',', '.', '!', '?']

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
pickle.dump(words, open('../backend/words.pkl', 'wb'))
pickle.dump(classes, open('../backend/classes.pkl', 'wb'))

# Using bag of words method for pattern match
# Bag of words: set the individual values to eithrer 0 or 1 if it occurs in that pattern
training = []
empty_output = [0] * len(classes)

for combo in combos:
    word_bag = []
    word_patterns = combo[0]
    word_patterns = [lemmatizer.lemmatize(word.lower())
                     for word in word_patterns]
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
train_x: list = list(training[:, 0])  # Features
train_y: list = list(training[:, 1])  # Labels

# Building neural-net model
# relu = rectified linear unit
# Sequential model orders and sequences i/o
# softmax = converts vector of numbers to vector of probabilities
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))  # prevents overfitting
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))  # prevents overfitting
model.add(Dense(len(train_y[0]), activation='softmax'))

# SGD: Stochastic Gradient Descent is an algo used to optimize i/o matches
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y),
                 epochs=300, batch_size=5, verbose='1')
model.save("backend/miniGPT_model.h5", hist)
print("\nTraining is Done!")
