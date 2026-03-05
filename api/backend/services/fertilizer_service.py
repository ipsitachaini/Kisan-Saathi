from sqlalchemy.orm import Session
from schemas.fertilizer import FertilizerRecommendRequest, FertilizerRecommendResponse, FertilizerData
from db.models import FertilizerReport
from core.fertilizer_config import (
    SYMPTOM_DEFICIENCY_MAP,
    DEFICIENCY_RECOMMENDATION,
    NPK_THRESHOLDS
)
from core.translation import translate

def recommend_fertilizer(db: Session, user_id: int, req: FertilizerRecommendRequest, lang: str = "en") -> FertilizerRecommendResponse:
    deficiency = "Balanced"
    
    if req.input_type == "symptoms" and req.symptoms:
        # Determine deficiency based on symptoms
        # Simple rule: use the first recognizing symptom from map
        for s in req.symptoms:
            if s in SYMPTOM_DEFICIENCY_MAP:
                deficiency = SYMPTOM_DEFICIENCY_MAP[s]
                break
    elif req.input_type == "npk":
        # Check against basic NPK thresholds
        # This is a naive model, as requested per requirements
        if req.n_value is not None and req.n_value < NPK_THRESHOLDS["N"]:
            deficiency = "Nitrogen (N) Deficiency"
        elif req.p_value is not None and req.p_value < NPK_THRESHOLDS["P"]:
            deficiency = "Phosphorus (P) Deficiency"
        elif req.k_value is not None and req.k_value < NPK_THRESHOLDS["K"]:
            deficiency = "Potassium (K) Deficiency"
            
    # Lookup recommendation
    rec = DEFICIENCY_RECOMMENDATION.get(deficiency, DEFICIENCY_RECOMMENDATION["Balanced"])
    fertilizer_name = rec["fertilizer_name"]
    quantity_per_acre = rec["quantity_per_acre"]
    
    total_quantity = quantity_per_acre * req.land_size
    symptoms_str = ",".join(req.symptoms) if req.symptoms else ""
    
    # Save report
    report = FertilizerReport(
        user_id=user_id,
        input_type=req.input_type,
        n_value=req.n_value,
        p_value=req.p_value,
        k_value=req.k_value,
        symptoms=symptoms_str,
        deficiency_detected=deficiency,
        fertilizer_name=fertilizer_name,
        quantity_per_acre=quantity_per_acre
    )
    
    db.add(report)
    db.commit()
    db.refresh(report)
    
    t_deficiency = translate(deficiency, lang)
    t_fertilizer = translate(fertilizer_name, lang)

    data = FertilizerData(
        deficiency_detected=t_deficiency,
        fertilizer_name=t_fertilizer,
        quantity_per_acre=quantity_per_acre,
        total_quantity=total_quantity,
        message_key="fertRecommendExplanation"
    )

    t_message = translate("fertRecommendExplanation", lang, deficiency=t_deficiency, fertilizer=t_fertilizer, total=round(total_quantity, 1))

    return FertilizerRecommendResponse(
        status="success",
        data=data,
        message=t_message
    )
