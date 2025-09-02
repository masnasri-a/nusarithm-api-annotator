
from fastapi import FastAPI
from app.api.v1 import router as v1_router
from app.api.emotion import router as emotion_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/v1", tags=["Sentiment Analysis"])
app.include_router(emotion_router, prefix="/v1", tags=["Emotion Analysis"])
from app.api.ner import router as ner_router
app.include_router(ner_router, prefix="/v1", tags=["Named Entity Recognition"])
