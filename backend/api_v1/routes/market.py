from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.schemas.market_price import MarketPriceRequest, MarketPriceResponse
from backend.services.market_service import get_market_prices
from backend.api_v1.dependencies import get_current_user
from backend.db.models import User

from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
def fetch_market_prices(
    req: MarketPriceRequest, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return get_market_prices(db, current_user.id, req, current_user.language)
