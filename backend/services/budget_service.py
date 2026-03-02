from sqlalchemy.orm import Session
from schemas.budget import BudgetCalculateRequest, BudgetCalculateResponse
from db.models import BudgetRecord
from core.budget_config import CROP_BUDGET_RATES
from core.translation import translate

def calculate_budget(db: Session, user_id: int, req: BudgetCalculateRequest, lang: str = "en") -> BudgetCalculateResponse:
    crop_keys = CROP_BUDGET_RATES.get(req.crop.lower())
    
    # default fallback if crop not found
    if not crop_keys:
        crop_keys = CROP_BUDGET_RATES["wheat"]
        
    labour = crop_keys["labour_cost_per_acre"] * req.land_size
    machine = crop_keys["machine_cost_per_acre"] * req.land_size
    diesel = crop_keys["diesel_cost_per_acre"] * req.land_size
    seed = crop_keys["seed_cost_per_acre"] * req.land_size
    fertilizer = crop_keys["fertilizer_cost_per_acre"] * req.land_size
    pesticide = crop_keys["pesticide_cost_per_acre"] * req.land_size
    
    estimated_cost = labour + machine + diesel + seed + fertilizer + pesticide
    remaining_budget = req.total_budget - estimated_cost
    is_sufficient = remaining_budget >= 0
    
    if is_sufficient:
        message_key = "budgetMessageSufficient"
    else:
        message_key = "budgetMessageInsufficient"
        
    record = BudgetRecord(
        user_id=user_id,
        total_budget=req.total_budget,
        land_size=req.land_size,
        crop=req.crop,
        labour_cost=labour,
        machine_cost=machine,
        diesel_cost=diesel,
        seed_cost=seed,
        fertilizer_cost=fertilizer,
        pesticide_cost=pesticide,
        estimated_cost=estimated_cost,
        remaining_budget=remaining_budget,
        is_sufficient=is_sufficient
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    
    return BudgetCalculateResponse(
        status="success",
        data={
            "labour_cost": labour,
            "machine_cost": machine,
            "diesel_cost": diesel,
            "seed_cost": seed,
            "fertilizer_cost": fertilizer,
            "pesticide_cost": pesticide,
            "estimated_cost": estimated_cost,
            "remaining_budget": remaining_budget,
            "is_sufficient": is_sufficient,
            "message_key": message_key
        },
        message=translate(message_key, lang, total=round(req.total_budget, 2), cost=round(estimated_cost, 2), remaining=round(remaining_budget, 2))
    )
