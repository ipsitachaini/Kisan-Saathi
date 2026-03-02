from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatMessageRequest(BaseModel):
    message: str

class ChatMessageResponse(BaseModel):
    id: int
    user_id: int
    message_text: str
    is_bot: bool
    timestamp: datetime

    class Config:
        from_attributes = True
