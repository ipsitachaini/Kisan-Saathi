from sqlalchemy.orm import Session
from schemas.market_price import MarketPriceRequest, MarketPriceResponse, MarketPriceData
from db.models import MarketLog
from core.market_config import MARKET_PRICES_DB
from core.translation import translate

def get_market_prices(db: Session, user_id: int, req: MarketPriceRequest, lang: str = "en") -> MarketPriceResponse:
    crop_prices = MARKET_PRICES_DB.get(req.crop_name.lower(), MARKET_PRICES_DB["wheat"])
    
    local = crop_prices["local_mandi"]
    district = crop_prices["district_market"]
    state = crop_prices["state_market"]
    demand = crop_prices["demand_trend"]
    advice_key = crop_prices["advice_key"]
    
    # Simple estimate logic: state market * quantity
    best_estimate = state * req.quantity_quintals
    
    # Save the log
    log = MarketLog(
        user_id=user_id,
        crop=req.crop_name,
        current_price=state,
        trend=demand,
        suggestion=advice_key
    )
    
    db.add(log)
    db.commit()
    
    data = MarketPriceData(
        crop_name=req.crop_name,
        local_mandi_price=local,
        district_market_price=district,
        state_market_price=state,
        demand_trend=demand,
        total_estimated_value=best_estimate,
        transport_advice_key=advice_key,
        message_key="mktPriceSuccess"
    )

    return MarketPriceResponse(
        status="success",
        data=data,
        message=translate("mktPriceSuccess", lang, value=best_estimate)
    )
