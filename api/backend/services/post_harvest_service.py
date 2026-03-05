from sqlalchemy.orm import Session
from schemas.post_harvest import PostHarvestInput, PostHarvestResponse, PostHarvestData
from db.models import User, PostHarvestRecord
from core.post_harvest_config import POST_HARVEST_DB
from core.translation import translate

def predict_post_harvest_risk(db: Session, user: User, input_data: PostHarvestInput, lang: str = "en") -> PostHarvestResponse:
    crop = input_data.crop_type.lower()
    config = POST_HARVEST_DB.get(crop, POST_HARVEST_DB["wheat"]) # fallback to wheat behavior
    
    base_risk = config["base_risk"]
    loss_pct = config["base_loss"]
    advice_key = "phAdvNormal"
    sell_suggestion_key = "suggHold"
    
    is_high_temp = input_data.temperature > config["max_temp"]
    is_high_hum = input_data.humidity > config["max_humidity"]
    
    if is_high_temp:
        base_risk += 0.3
        loss_pct += 15.0
        advice_key = config["advice_high_temp"]
        sell_suggestion_key = "suggSellNow"
    
    # Humidity overrides temp advice if its worse (usually true for fungal/spoilage context)
    if is_high_hum:
        base_risk += 0.4
        loss_pct += 20.0
        advice_key = config["advice_high_hum"]
        # if already sell now from temp, keep that. 
        if sell_suggestion_key != "suggSellNow":
            sell_suggestion_key = "suggSellSoon"
            
    # Duration factor
    if input_data.storage_duration > 30:
        base_risk += 0.2
        loss_pct += 5.0
        
    risk_score = min(0.99, base_risk)
    loss_percentage = min(100.0, loss_pct)
    
    # Normalize sell suggestion dynamically
    if risk_score > 0.7:
        sell_suggestion_key = "suggSellNow"
    elif risk_score > 0.4 and sell_suggestion_key == "suggHold":
        sell_suggestion_key = "suggSellSoon"

    record = PostHarvestRecord(
        user_id=user.id,
        crop_type=input_data.crop_type,
        storage_method=input_data.storage_method,
        temperature=input_data.temperature,
        humidity=input_data.humidity,
        storage_duration=input_data.storage_duration,
        location=input_data.location,
        spoilage_risk_score=round(risk_score, 2),
        loss_percentage=round(loss_percentage, 1),
        storage_advice=advice_key,
        sell_suggestion=sell_suggestion_key
    )
    
    db.add(record)
    db.commit()
    db.refresh(record)
    
    data = PostHarvestData.from_orm(record)
    data.storage_advice = translate(record.storage_advice, lang)
    data.sell_suggestion = translate(record.sell_suggestion, lang)

    return PostHarvestResponse(
        status="success",
        data=data,
        message=translate("phSuccessMsg", lang)
    )
