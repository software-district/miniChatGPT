# Welcome to miniChatGPT Repo: A light-weight example of chatGPT

## How to setup and run miniChatGPT

### 1. Clone Project

   > git clone https://github.com/eruigu/miniChatGPT.git

### 2. Setup Environment

   > install python3, pip, python3.9-venv

### 3. Create virtual environment

   > python3 -m venv venv

### 4. Activate virtual environment and update pip

   > source venv/bin/activate && pip install -U pip setuptools

### 5. Install wheel library

   > pip install wheel

### 6. Install dependencies

   > pip install -r requirements.txt

### 7. Train chatbot model

   > python3 training.py: which is located in model_training/

### 8. Run the chatbot

   > python3 server.py: which is located in backend/
    > the app will run on 127.0.0.1:8001
