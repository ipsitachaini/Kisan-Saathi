from pydantic import BaseModel

class BudgetCalculateRequest(BaseModel):
    total_budget: float
    land_size: float
    crop: str

class BudgetData(BaseModel):
    labour_cost: float
    machine_cost: float
    diesel_cost: float
    seed_cost: float
    fertilizer_cost: float
    pesticide_cost: float
    estimated_cost: float
    remaining_budget: float
    is_sufficient: bool
    message_key: str

class BudgetCalculateResponse(BaseModel):
    status: str
    data: BudgetData
    message: str
