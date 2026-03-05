from sqlalchemy.orm import Session
from backend.schemas.dashboard import DashboardSummary, WeatherSummary, RecentActivity
from backend.db.models import User, PostHarvestRecord, LeafScanRecord

def get_dashboard_summary(db: Session, user: User) -> DashboardSummary:
    # 1. Fetch Mock Weather Data (to be replaced by external API in integration phase)
    weather = WeatherSummary(
        temperature=28.5,
        condition="Sunny",
        location=user.full_name or "Local Farm" # Placeholder location
    )
    
    # 2. Fetch Recent Activities (Scans + Post Harvest)
    activities = []
    
    # Get last 3 post harvest records
    ph_records = db.query(PostHarvestRecord).filter(
        PostHarvestRecord.user_id == user.id
    ).order_by(PostHarvestRecord.created_at.desc()).limit(3).all()
    
    for r in ph_records:
        activities.append(RecentActivity(
            id=r.id,
            type="post_harvest",
            date=r.created_at,
            summary=f"Stored {r.crop_type} - {r.sell_suggestion}"
        ))
        
    # Get last 3 leaf scans
    scan_records = db.query(LeafScanRecord).filter(
        LeafScanRecord.user_id == user.id
    ).order_by(LeafScanRecord.scan_date.desc()).limit(3).all()
    
    for s in scan_records:
        activities.append(RecentActivity(
            id=s.id,
            type="scan",
            date=s.scan_date,
            summary=f"Scan: {s.disease_prediction} ({int(s.confidence_score * 100)}%)"
        ))
        
    # Sort combined activities by date descending
    activities.sort(key=lambda x: x.date, reverse=True)
    activities = activities[:5] # Keep top 5 latest
    
    # 3. Generate Mock Alerts
    alerts = []
    if len(activities) == 0:
        alerts.append("Welcome! Try scanning a leaf or adding storage data.")
    
    return DashboardSummary(
        weather=weather,
        recent_activity=activities,
        active_alerts=alerts
    )
