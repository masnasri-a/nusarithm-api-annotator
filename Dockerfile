# Dockerfile for FastAPI Sentiment API
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install system dependencies for transformers/torch
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app ./app

# Expose port
EXPOSE 8111

# Run API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8111"]
