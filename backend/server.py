import os
import json
import pickle
import tensorflow as tf

from chatbot import predict_res, get_random_res
from flask import Flask, render_template, request
from config import Config, DevConfig

load_model = tf.keras.models.load_model

CWD = os.getcwd()
intents_path = os.path.join(CWD, '../model_training/intents.json')

model = load_model('miniGPT_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
intents = json.loads(open(intents_path).read())

bot = Flask(__name__,
            static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATES_FOLDER
            )
bot.config.from_object(DevConfig)


@bot.route("/")
def home():
    return render_template('chat.html')


@bot.route("/get", methods=["POST"])
def run_chatbot_web():
    message = request.form["message"]
    if message.startswith('my name is'):
        name = message[11:]
        ints = predict_res(message)
        res0 = get_random_res(ints, intents)
        res = res0.replace("{n}", name)
    elif message.startswith('my name is'):
        name = message[14:]
        ints = predict_res(message)
        res0 = get_random_res(ints, intents)
        res = res0.replace("{n}", name)
    else:
        ints = predict_res(message)
        res = get_random_res(ints, intents)
    return res


if __name__ == "__main__":
    bot.run(host='0.0.0.0', port=8001)
