# Nusarithm Annotator API

Lightweight FastAPI service for text annotation tasks (sentiment & emotion) using Indonesian pretrained Transformers.

## Overview

This repository provides a small, production-friendly FastAPI app that exposes simple endpoints for:
- Sentiment analysis
- Emotion classification

Models are loaded once at startup to keep RAM and CPU usage low on small servers.

## Quickstart

Prerequisites: Python 3.10+, Docker (optional).

Local (virtualenv):

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

With Docker Compose:

```bash
docker-compose up --build
```

The API will be available at http://localhost:8000. Open http://localhost:8000/docs for interactive docs.

## Endpoints

Base prefix: `/v1`

- `POST /v1/sentiment` - Sentiment prediction
	- Body: `{ "text": "..." }`
	- Response: `{ "sentiment": "LABEL", "confidence": 0.9876 }`

- `POST /v1/emotion` - Emotion prediction
	- Body: `{ "text": "..." }`
	- Response: `{ "emotion": "LABEL", "confidence": 0.9876 }`

## Notes & recommendations

- Models are downloaded from the Hugging Face Hub on first startup. Provide a persistent cache (via `TRANSFORMERS_CACHE`) when running in containers to avoid repeated downloads.
- For very small instances, prefer CPU builds and lower concurrency for `uvicorn` (workers=1).

## Credits

Project and code by masnasri-a — https://github.com/masnasri-a/nusarithm-api-annotator#

## CI / CD (GitHub Actions)

This repository includes a GitHub Actions workflow that builds the Docker image and pushes it to Docker Hub when commits are pushed to `main`.

Secrets required (Repository settings -> Secrets -> Actions):
- `DOCKERHUB_USERNAME` - your Docker Hub username (e.g. `masnasria26`)
- `DOCKERHUB_TOKEN` - a Docker Hub access token (do not commit your password or token to the repo)

The workflow file is located at `.github/workflows/docker-publish.yml` and tags the image as `masnasria26/nusarithm-anno-api:latest`.


