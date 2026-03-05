from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.crop_recommend import CropRecommendationRequest, CropRecommendationResponse
from services.crop_recommend_service import recommend_crops
from api_v1.dependencies import get_current_user
from db.models import User

router = APIRouter()

@router.post("")
def get_crop_recommendation(
    req: CropRecommendationRequest, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    print("--- CROP RECOMMENDATION HIT ---")
    print("Request Payload:", req.dict())
    print("User Language Code:", current_user.language)
    print("User Context:", current_user.email)
    print("-------------------------------")

    from fastapi.responses import JSONResponse
    return JSONResponse(content={
      "status": "success",
      "data": {
        "recommended_crops": ["rice", "maize", "groundnut"]
      },
      "message": "Test recommendation working."
    })
