# Minimal, production-friendly Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install only minimal system packages required for downloading wheels
RUN apt-get update \
	&& apt-get install -y --no-install-recommends ca-certificates git curl \
	&& rm -rf /var/lib/apt/lists/*

# Copy only requirements first for Docker layer caching
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install Python deps without cache
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir --prefer-binary -r /app/requirements.txt \
	&& rm -rf /root/.cache/pip

# Add a non-root user and copy the application
RUN useradd -m -s /bin/bash appuser
COPY app /app/app
RUN chown -R appuser:appuser /app

USER appuser

ENV TRANSFORMERS_CACHE=/app/cache
VOLUME ["/app/cache"]

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
