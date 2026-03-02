from pydantic import BaseModel

class YieldPredictRequest(BaseModel):
    crop_name: str
    land_size: float
    soil_quality: str # good, medium, poor
    irrigation_availability: bool
    rainfall_level: str # high, normal, low

class YieldPredictData(BaseModel):
    expected_yield: float
    expected_revenue: float
    message_key: str

class YieldPredictResponse(BaseModel):
    status: str
    data: YieldPredictData
    message: str
