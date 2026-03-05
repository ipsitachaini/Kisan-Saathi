from pydantic import BaseModel
from typing import Any

class MarketPriceRequest(BaseModel):
    crop_name: str
    quantity_quintals: float

class MarketPriceData(BaseModel):
    crop_name: str
    local_mandi_price: float
    district_market_price: float
    state_market_price: float
    demand_trend: str
    total_estimated_value: float # based on best available price (state)
    transport_advice_key: str
    message_key: str

class MarketPriceResponse(BaseModel):
    status: str
    data: MarketPriceData
    message: str

