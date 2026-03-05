from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api_v1.dependencies import get_current_user
from backend.db.database import get_db
from backend.db.models import User
from backend.schemas.chatbot import ChatMessageRequest, ChatMessageResponse
from backend.services import chatbot_service

router = APIRouter()

@router.post("/chat", response_model=ChatMessageResponse)
def send_chat_message(
    request: ChatMessageRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Send a message to the Kisan Saathi AI assistant and receive a response.
    Returns the bot's response log.
    """
    user_log, bot_log = chatbot_service.process_chat_message(db, current_user, request)
    return bot_log
