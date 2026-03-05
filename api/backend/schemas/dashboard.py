from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WeatherSummary(BaseModel):
    temperature: float
    condition: str
    location: str

class RecentActivity(BaseModel):
    id: int
    type: str # 'scan', 'post_harvest'
    date: datetime
    summary: str

class DashboardSummary(BaseModel):
    weather: Optional[WeatherSummary] = None
    recent_activity: List[RecentActivity] = []
    active_alerts: List[str] = []
