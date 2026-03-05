from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from backend.api_v1.dependencies import get_current_user
from backend.db.database import get_db
from backend.db.models import User
from backend.schemas.leaf_scan import LeafScanResponse
from backend.services import leaf_scan_service

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
