
from fastapi import FastAPI
from app.api.v1 import router as v1_router
from app.api.emotion import router as emotion_router

app = FastAPI()
app.include_router(v1_router, prefix="/v1")
app.include_router(emotion_router, prefix="/v1")
