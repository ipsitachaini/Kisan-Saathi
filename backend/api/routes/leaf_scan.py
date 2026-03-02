from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from api.dependencies import get_current_user
from db.database import get_db
from db.models import User
from schemas.leaf_scan import LeafScanResponse
from services import leaf_scan_service

router = APIRouter()

@router.post("/upload", response_model=LeafScanResponse)
def upload_leaf_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload an image of a crop leaf for AI disease detection.
    """
    record = leaf_scan_service.process_leaf_scan(db, current_user, file)
    return record
