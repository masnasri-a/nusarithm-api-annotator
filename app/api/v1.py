from fastapi import APIRouter
from app.models.review import ReviewRequest
from app.services.sentiment import predict_sentiment
import time

router = APIRouter()

@router.post("/sentiment")
async def predict(request: ReviewRequest):
    start_time = time.time()
    result = await predict_sentiment(request.text)
    execution_time = time.time() - start_time
    return {"result": result, "execution_time": execution_time}
