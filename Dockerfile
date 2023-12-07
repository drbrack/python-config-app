FROM python:3.8-slim

WORKDIR /app

COPY app.py .
COPY config.json .

CMD ["python", "-u", "/app/app.py"]
