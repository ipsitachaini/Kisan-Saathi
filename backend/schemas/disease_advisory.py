from pydantic import BaseModel
from typing import List

class DiseaseAdvisoryRequest(BaseModel):
    symptoms: List[str]

class DiseaseData(BaseModel):
    possible_issue: str
    treatment: str
    prevention: str
    cost_estimate: float
    message_key: str

class DiseaseAdvisoryResponse(BaseModel):
    status: str
    data: DiseaseData
    message: str
