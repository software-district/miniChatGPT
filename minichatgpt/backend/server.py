import os
import pickle
import tensorflow as tf

from flask import Flask, render_template, request
from minichatgpt.config import Config, DevConfig
from minichatgpt.model_training.training import intents
from minichatgpt.backend.chatbot import predict_res, get_random_res

load_model = tf.keras.models.load_model

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'miniGPT_model.h5')
words_path = os.path.join(current_dir, 'words.pkl')
classes_path = os.path.join(current_dir, 'classes.pkl')

model = load_model(model_path)
words = pickle.load(open(words_path, 'rb'))
classes = pickle.load(open(classes_path, 'rb'))

bot = Flask(__name__,
            static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATES_FOLDER
            )
bot.config.from_object(DevConfig)


@bot.route("/")
def home():
    return render_template("chat.html")


@bot.route("/get", methods=["POST"])
def run_chatbot_web():
    message = request.form["message"].lower()
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
