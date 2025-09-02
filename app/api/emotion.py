from fastapi import APIRouter
from app.models.emotion import EmotionRequest
from app.services.emotion import predict_emotion

router = APIRouter()

@router.post("/emotion")
async def emotion_predict(request: EmotionRequest):
    result = await predict_emotion(request.text)
    return result
