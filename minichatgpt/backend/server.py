import os
import pickle
import tensorflow as tf

from flask import Flask, render_template, request, jsonify
from minichatgpt.config import Config, DevConfig
from minichatgpt.model_training.training import intents
from minichatgpt.backend.chatbot import predict_res, get_random_res
from minichatgpt.openai_gpt.openai_service import generate_response

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

@bot.route("/openai", methods=["GET"])
def openai_page():
    return render_template('openai.html')

@bot.route('/api/chat', methods=['POST'])
def processResponse():
    # Get the user message from the request
    user_message = request.json['message']

    # Generate the system's response using OpenAI logic
    system_response = generate_response(user_message)

    # Return the system response as JSON
    return jsonify({'response': system_response})


if __name__ == "__main__":
    # Check if running in production
    if os.getenv("FLASK_ENV") == "production":
        host = "0.0.0.0"
    else:
        host = "127.0.0.1"

    # Retrieve the PORT environment variable if available, otherwise use default value
    port = int(os.getenv("PORT", 8001))

    bot.run(host=host, port=port)
