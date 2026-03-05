from pydantic import BaseModel
from datetime import datetime

class LeafScanResponse(BaseModel):
    id: int
    image_url: str
    disease_prediction: str
    confidence_score: float # 0.0 to 1.0
    scan_date: datetime
    
    class Config:
        from_attributes = True
