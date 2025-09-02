# Nusarithm Sentiment API

API analisis sentimen berbasis FastAPI dan IndoBERT, terstruktur dengan design pattern (service, model, router) dan siap digunakan di server kecil.

## Fitur
- Endpoint `/v1/predict` untuk analisis sentimen teks Bahasa Indonesia
- Model hanya di-load sekali saat API start
- Async dan ringan
- Struktur folder terpisah (app/api, app/models, app/services)
- Docker & Docker Compose siap pakai

## Cara Menjalankan
### Lokal
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan API:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Docker
1. Build dan jalankan:
   ```bash
   docker-compose up --build
   ```
2. API tersedia di port 8000

## Struktur Folder
```
app/
  api/
  models/
  services/
  main.py
requirements.txt
Dockerfile
docker-compose.yml
```

## Endpoint
- `POST /v1/predict`
  - Body: `{ "text": "ulasan produk" }`
  - Response: `{ "sentiment": "LABEL", "confidence": 0.9876 }`

## Lisensi
Bebas digunakan untuk riset dan pengembangan.
