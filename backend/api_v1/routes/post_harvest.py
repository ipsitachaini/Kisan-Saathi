from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api_v1.dependencies import get_current_user
from backend.db.database import get_db
from backend.db.models import User
from backend.schemas.post_harvest import PostHarvestInput, PostHarvestResponse
from backend.services import post_harvest_service

router = APIRouter()

@router.post("", response_model=PostHarvestResponse)
def predict_spoilage(
    input_data: PostHarvestInput,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Predict storage spoilage risk.
    """
    return post_harvest_service.predict_post_harvest_risk(db, current_user, input_data, current_user.language)
