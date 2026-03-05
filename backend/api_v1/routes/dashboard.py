from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_v1.dependencies import get_current_user
from db.database import get_db
from db.models import User
from schemas.dashboard import DashboardSummary
from services import dashboard_service

router = APIRouter()

@router.get("/summary", response_model=DashboardSummary)
def get_summary(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    """
    Get the aggregated dashboard summary for the current user.
    """
    return dashboard_service.get_dashboard_summary(db, current_user)
