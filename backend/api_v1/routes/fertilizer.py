from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.schemas.fertilizer import FertilizerRecommendRequest, FertilizerRecommendResponse
from backend.services.fertilizer_service import recommend_fertilizer
from backend.api_v1.dependencies import get_current_user
from backend.db.models import User

router = APIRouter()

@router.post("", response_model=FertilizerRecommendResponse)
def get_fertilizer_recommendation(
    req: FertilizerRecommendRequest, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return recommend_fertilizer(db, current_user.id, req, current_user.language)
