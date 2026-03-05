from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.market_price import MarketPriceRequest, MarketPriceResponse
from services.market_service import get_market_prices
from api.dependencies import get_current_user
from db.models import User

from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
def fetch_market_prices(
    req: MarketPriceRequest, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return get_market_prices(db, current_user.id, req, current_user.language)
