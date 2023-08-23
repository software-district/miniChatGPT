FROM python:3.9-slim

WORKDIR /app

COPY . .

# Set environment variables
ENV FLASK_ENV=production
ENV PORT=8001

RUN pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

RUN python -u minichatgpt/model_training/training.py

ENV OPENAI_API_KEY

EXPOSE 8001

ENTRYPOINT ["python", "-u", "minichatgpt/backend/server.py"]
