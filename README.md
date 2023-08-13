# Welcome to miniChatGPT!

    A light-weight example of chatGPT using neural nets and custom trained model

   https://user-images.githubusercontent.com/60236247/235518311-ae1c71fc-baa5-40ec-ab00-6edfdc4fba2d.mov

## Tech Stack
* [TensorFlow](https://www.tensorflow.org/) is an end-to-end open-source platform for machine learning
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) is a micro web framework written in Python
* [NLTK](https://www.nltk.org/) is a leading platform for building Python programs to work with human language data
* Python, HTML/CSS

## How to set up and run miniChatGPT

### 1. Clone Project

   > git clone [https://github.com/eruigu/miniChatGPT.git]

### 2. Setup Environment

   > install python3: check the version "python3 --version"

   > MacOS: pip3 install virtualenv

   > Linux (Debian): sudo apt install pythonx.x-venv (replace x with your version of python)

### 3. Create virtual environment

   > python3 -m venv venv

### 4. Activate virtual environment and update pip

   > source venv/bin/activate && pip install -U pip setuptools

### 5. Install wheel library

   > MacOS: pip3 install wheel

   > Linux (Debian): pip install wheel

### 6. Install dependencies

   > MacOS: pip3 install -r requirements.txt

   > Linux (Debian): pip install -r requirements.txt

### 7. Train chatbot model

   > `python3 -m minichatgpt.model_training.training`
   >> This will create two .pkl (pickle) files: classes and words & miniGPT_model.h5 in src/backend/

### 8. Run the chatbot

   > `python3 -m minichatgpt.backend.server`
   >> this will create a .h5 model file in the current directory

### 9. The server is running on 127.0.0.1:8001

   > You can change the server config in server.py

### 10. Docker

   > `docker docker build -t minichatgpt:1.0.0 .`
   >> this will create an image for the project

   > `docker run --name minichatgpt -d -p 8001:8001 minichatgpt:1.0.0`
   >> this creates and runs a container for the image in the background.
   >>> access at localhost:8001
