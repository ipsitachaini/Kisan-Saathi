from sqlalchemy.orm import Session
from schemas.disease_advisory import DiseaseAdvisoryRequest, DiseaseAdvisoryResponse, DiseaseData
from db.models import DiseaseReport
from core.disease_config import DISEASE_DB, SYMPTOM_DISEASE_MAP
from core.translation import translate

def get_disease_advisory(db: Session, user_id: int, req: DiseaseAdvisoryRequest, lang: str = "en") -> DiseaseAdvisoryResponse:
    determined_disease_id = "unknown"
    
    # naive first-match based on symptoms
    for symptom in req.symptoms:
        if symptom in SYMPTOM_DISEASE_MAP:
            determined_disease_id = SYMPTOM_DISEASE_MAP[symptom]
            break
            
    disease_info = DISEASE_DB[determined_disease_id]
    
    symptoms_str = ",".join(req.symptoms)
    
    report = DiseaseReport(
        user_id=user_id,
        symptoms=symptoms_str,
        possible_issue=disease_info["name"],
        treatment=disease_info["treatment"],
        prevention=disease_info["prevention"],
        cost_estimate=disease_info["cost_estimate"]
    )
    
    db.add(report)
    db.commit()
    db.refresh(report)
    
    t_disease = translate(disease_info["name"], lang)
    t_treatment = translate(disease_info["treatment"], lang)

    data = DiseaseData(
        possible_issue=t_disease,
        treatment=t_treatment,
        prevention=translate(disease_info["prevention"], lang),
        cost_estimate=disease_info["cost_estimate"],
        message_key="disease_summary"
    )

    t_message = translate("disease_summary", lang, disease=t_disease, treatment=t_treatment, cost=disease_info["cost_estimate"])

    return DiseaseAdvisoryResponse(
        status="success",
        data=data,
        message=t_message
    )
