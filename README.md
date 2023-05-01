# Welcome to miniChatGPT

    A light-weight example of chatGPT using neural nets and an intents file
    Blog post coming soon!
    
   https://user-images.githubusercontent.com/60236247/235518311-ae1c71fc-baa5-40ec-ab00-6edfdc4fba2d.mov

## How to setup and run miniChatGPT

### 1. Clone Project

   > git clone [https://github.com/eruigu/miniChatGPT.git]

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

### 9. Server is running on 127.0.0.1:8001

   > You can change server function in server.py
