FROM ubuntu:latest
LABEL authors="Vasyaka-porosyaka"

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
#ENV APP_ENV=production

EXPOSE 8000

# Run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
