FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
COPY app/api /app/api
COPY app/core /app/core
COPY app/db /app/db
COPY app/schemas /app/schemas
COPY app/utils /app/utils
COPY app/background.py /app/background.py
COPY app/main.py /app/main.py

RUN pip3 install --no-cache-dir -r requirements.txt

ENV KAFKA_BOOTSTRAP_SERVERS="kafka:29092" \
    KAFKA_TOPIC="recommendations_topic" \
    MONGODB_URI="mongodb://root:root@mongodb:27017" \
    MONGODB_DATABASE="recommendations" \
    OPENAI_KEY="replace_openai_api_here"

EXPOSE 8000
# Run the FastAPI service and background process
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & python background.py"]