from pydantic import BaseModel

class EmotionRequest(BaseModel):
    text: str
