# Configured market prices per quintal in different simulated regions
MARKET_PRICES_DB = {
    "wheat": {
        "local_mandi": 2200.0,
        "district_market": 2350.0,
        "state_market": 2500.0,
        "demand_trend": "steady", # 'high', 'steady', 'low'
        "advice_key": "mktAdvWheat"
    },
    "rice": {
        "local_mandi": 2000.0,
        "district_market": 2150.0,
        "state_market": 2300.0,
        "demand_trend": "high",
        "advice_key": "mktAdvRice"
    },
    "tomato": {
        "local_mandi": 1500.0, # highly variable, using stable avg
        "district_market": 1800.0,
        "state_market": 2200.0,
        "demand_trend": "high",
        "advice_key": "mktAdvTomato"
    },
    "potato": {
        "local_mandi": 1200.0,
        "district_market": 1400.0,
        "state_market": 1600.0,
        "demand_trend": "steady",
        "advice_key": "mktAdvPotato"
    },
    "onion": {
        "local_mandi": 1800.0,
        "district_market": 2100.0,
        "state_market": 2600.0,
        "demand_trend": "high",
        "advice_key": "mktAdvOnion"
    },
    "millets": {
        "local_mandi": 2500.0,
        "district_market": 2800.0,
        "state_market": 3100.0,
        "demand_trend": "high",
        "advice_key": "mktAdvMillets"
    }
}
