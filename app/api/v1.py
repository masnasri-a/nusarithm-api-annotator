from fastapi import APIRouter, HTTPException
from app.models.review import ReviewRequest
from app.services.sentiment import predict_sentiment
import time

router = APIRouter()

@router.post("/sentiment")
async def predict(request: ReviewRequest):
    start_time = time.time()
    try:
        result = await predict_sentiment(request.text)
        execution_time = time.time() - start_time
        return {"result": result, "execution_time": execution_time}
    except Exception as e:
        execution_time = time.time() - start_time
        raise HTTPException(status_code=500, detail={"error": str(e), "execution_time": execution_time})
