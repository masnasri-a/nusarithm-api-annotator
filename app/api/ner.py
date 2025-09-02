from fastapi import APIRouter, HTTPException
from app.models.ner import NERRequest
from app.services.ner import predict_ner
import time

router = APIRouter()


@router.post("/ner")
async def ner_predict(request: NERRequest):
    start = time.time()
    try:
        result = await predict_ner(request.text)
        exec_time = time.time() - start
        return {"result": result, "execution_time": exec_time}
    except Exception as e:
        exec_time = time.time() - start
        raise HTTPException(status_code=500, detail={"error": str(e), "execution_time": exec_time})
