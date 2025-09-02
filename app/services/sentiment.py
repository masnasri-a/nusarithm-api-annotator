
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import asyncio

MODEL_NAME = "siRendy/indobert-analisis-sentimen-review-produk-datathon2025"
# Load model & pipeline only once when module is imported
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
device = 0 if torch.cuda.is_available() else -1
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=device)

async def predict_sentiment(text: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, classifier, text)
    return {
        "sentiment": result[0]["label"],
        "confidence": round(result[0]["score"], 4)
    }
