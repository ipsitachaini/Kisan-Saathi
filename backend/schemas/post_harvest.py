from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostHarvestInput(BaseModel):
    crop_type: str
    storage_method: str
    temperature: float
    humidity: float
    storage_duration: int
    location: str

class PostHarvestData(BaseModel):
    id: int
    spoilage_risk_score: float # 0.0 to 1.0
    loss_percentage: float
    storage_advice: str
    sell_suggestion: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PostHarvestResponse(BaseModel):
    status: str
    data: PostHarvestData
    message: str
