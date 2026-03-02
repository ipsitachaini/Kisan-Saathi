from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.disease_advisory import DiseaseAdvisoryRequest, DiseaseAdvisoryResponse
from services.disease_service import get_disease_advisory
from api.dependencies import get_current_user
from db.models import User

router = APIRouter()

@router.post("", response_model=DiseaseAdvisoryResponse)
def fetch_disease_advisory(
    req: DiseaseAdvisoryRequest, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return get_disease_advisory(db, current_user.id, req, current_user.language)
