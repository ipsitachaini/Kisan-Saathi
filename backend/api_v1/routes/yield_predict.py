from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.schemas.yield_predict import YieldPredictRequest, YieldPredictResponse
from backend.services.yield_service import predict_yield
from backend.api_v1.dependencies import get_current_user
from backend.db.models import User

router = APIRouter()

@router.post("/estimate", response_model=YieldPredictResponse)
def estimate_yield(req: YieldPredictRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return predict_yield(db, current_user.id, req, current_user.language)
