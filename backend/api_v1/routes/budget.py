from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.budget import BudgetCalculateRequest, BudgetCalculateResponse
from services.budget_service import calculate_budget
from api_v1.dependencies import get_current_user
from db.models import User

router = APIRouter()

@router.post("/calculate", response_model=BudgetCalculateResponse)
def calculate_farm_budget(req: BudgetCalculateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return calculate_budget(db, current_user.id, req, current_user.language)
