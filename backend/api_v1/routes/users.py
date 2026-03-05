from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.models import User
from backend.schemas.user import UserResponse
from backend.api_v1.dependencies import get_current_user
from pydantic import BaseModel

class LanguageUpdate(BaseModel):
    language: str

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Get current user profile.
    """
    return current_user

@router.put("/me/language", response_model=UserResponse)
def update_user_language(
    lang_update: LanguageUpdate, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """
    Update current user's preferred language.
    """
    current_user.language = lang_update.language
    db.commit()
    db.refresh(current_user)
    return current_user
