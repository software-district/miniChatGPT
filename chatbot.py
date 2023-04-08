import json
import random
import pickle
import numpy as np
import tensorflow as tf 

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
load_model = tf.keras.models.load_model

model = load_model('miniGPT_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Clean sentence for parsing 
def clean_sentence(sentence: str):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
    
# Using bag of words method: convert words to 0 or 1 if they are recognized
def bag_of_words(sentence: str):
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Predict response based on input 
def predict_res(sentence: str):
    ERROR_THRESHOLD = 0.25
    b_of_w = bag_of_words(sentence)
    res = model.predict(np.array([b_of_w]))[0]

    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x:x[1],reverse=True)
    res_list: list = []

    for r in results:
        res_list.append({'intent':classes[r[0]], 'probability': str(r[1])})
    return res_list

def get_random_res(intents_list: list, intents_json: dict):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            ran_res = random.choice(i['responses'])
            break
    return ran_res

def run_chatbot():
    print('miniChatGPT is listening! Say anything')
    while True:
        message = input('')
        ints = predict_res(message)
        res = get_random_res(ints, intents)
        print(res)


run_chatbot()
