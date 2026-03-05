from sqlalchemy.orm import Session
from backend.schemas.crop_recommend import CropRecommendationRequest, CropRecommendationResponse, CropRecommendationData, RecommendedCropItem
from backend.db.models import CropRecommendation
from backend.core.crop_recommend_config import CROP_DB
from backend.core.translation import translate

def recommend_crops(db: Session, user_id: int, req: CropRecommendationRequest, lang: str = "en") -> CropRecommendationResponse:
    # simple filtering algorithm
    matches = []
    
    for c in CROP_DB:
        if req.soil_type in c["soil"] and req.season in c["season"] and req.water_availability in c["water"]:
            matches.append(c)
            
    # if no exact matches, just randomly pick something or show default. For this we will loosen water restriction first
    if not matches:
        for c in CROP_DB:
            if req.soil_type in c["soil"] and req.season in c["season"]:
                matches.append(c)

    # Convert to response objects
    recommendations = []
    
    # Take top 3 recommendations
    for match in matches[:3]:
        total_profit = match["expected_profit_per_acre"] * req.land_size
        
        item = RecommendedCropItem(
            crop_name=translate(match["crop"], lang),
            days_to_harvest=match["days_to_harvest"],
            expected_profit_per_acre=match["expected_profit_per_acre"],
            total_expected_profit=total_profit,
            advice_key=match["advice_key"]
        )
        recommendations.append(item)
        
    # Save to DB correctly
    import json
    crops_json = json.dumps([r.crop_name for r in recommendations])
    report = CropRecommendation(
        user_id=user_id,
        soil_type=req.soil_type,
        rainfall=req.water_availability, # map loosely
        state=req.season, # map loosely
        top_crops=crops_json
    )
    db.add(report)
    db.commit()
    
    msg_key = "cropRecommendSuccess" if recommendations else "cropRecommendFail"
    
    data = CropRecommendationData(
        recommendations=recommendations,
        message_key=msg_key
    )

    t_message = translate("cropRecommendSuccess", lang) if recommendations else translate("cropRecommendFail", lang)

    return CropRecommendationResponse(
        status="success",
        data=data,
        message=t_message
    )
