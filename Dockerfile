FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

RUN python -u minichatgpt/model_training/training.py

EXPOSE 8001

ENTRYPOINT ["python", "-u", "minichatgpt/backend/server.py"]
