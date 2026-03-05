from pydantic import BaseModel
from typing import Optional, List

class FertilizerRecommendRequest(BaseModel):
    input_type: str # 'npk' or 'symptoms'
    n_value: Optional[float] = None
    p_value: Optional[float] = None
    k_value: Optional[float] = None
    symptoms: Optional[List[str]] = None
    land_size: float # acres

class FertilizerData(BaseModel):
    deficiency_detected: str
    fertilizer_name: str
    quantity_per_acre: float
    total_quantity: float
    message_key: str

class FertilizerRecommendResponse(BaseModel):
    status: str
    data: FertilizerData
    message: str
