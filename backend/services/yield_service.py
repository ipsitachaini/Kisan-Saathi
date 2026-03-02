from sqlalchemy.orm import Session
from schemas.yield_predict import YieldPredictRequest, YieldPredictResponse
from db.models import YieldPrediction
from core.yield_config import (
    BASE_YIELD_PER_ACRE,
    BASE_PRICE_PER_QUINTAL,
    SOIL_QUALITY_MULTIPLIER,
    IRRIGATION_MULTIPLIER,
    RAINFALL_MULTIPLIER
)
from core.translation import translate

def predict_yield(db: Session, user_id: int, req: YieldPredictRequest, lang: str = "en") -> YieldPredictResponse:
    crop = req.crop_name.lower()
    
    # Defaults if missing
    base_yield = BASE_YIELD_PER_ACRE.get(crop, 20.0)
    base_price = BASE_PRICE_PER_QUINTAL.get(crop, 1500)
    
    soil_mult = SOIL_QUALITY_MULTIPLIER.get(req.soil_quality.lower(), 0.8)
    irrigation_mult = IRRIGATION_MULTIPLIER.get(req.irrigation_availability, 0.7)
    rainfall_mult = RAINFALL_MULTIPLIER.get(req.rainfall_level.lower(), 1.0)
    
    # Calculate expected yield per acre
    yield_per_acre = base_yield * soil_mult * irrigation_mult * rainfall_mult
    
    # Total yield
    total_expected_yield_quintals = yield_per_acre * req.land_size
    
    # Expected revenue
    expected_revenue = total_expected_yield_quintals * base_price
    
    record = YieldPrediction(
        user_id=user_id,
        crop_name=crop,
        land_size=req.land_size,
        soil_quality=req.soil_quality.lower(),
        irrigation_availability=req.irrigation_availability,
        rainfall_level=req.rainfall_level.lower(),
        expected_yield=total_expected_yield_quintals,
        expected_revenue=expected_revenue
    )
    
    db.add(record)
    db.commit()
    db.refresh(record)
    t_message = translate("yieldExplanation", lang, **{"yield": round(total_expected_yield_quintals, 2), "revenue": round(expected_revenue, 2)})
    
    return YieldPredictResponse(
        status="success",
        data={
            "expected_yield": total_expected_yield_quintals,
            "expected_revenue": expected_revenue,
            "message_key": "yieldExplanation"
        },
        message=t_message
    )
