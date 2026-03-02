from pydantic import BaseModel
from typing import List, Any

class CropRecommendationRequest(BaseModel):
    soil_type: str
    season: str
    water_availability: str
    land_size: float

class RecommendedCropItem(BaseModel):
    crop_name: str
    days_to_harvest: str
    expected_profit_per_acre: float
    total_expected_profit: float
    advice_key: str

class CropRecommendationData(BaseModel):
    recommendations: List[RecommendedCropItem]
    message_key: str

class CropRecommendationResponse(BaseModel):
    status: str
    data: CropRecommendationData
    message: str

