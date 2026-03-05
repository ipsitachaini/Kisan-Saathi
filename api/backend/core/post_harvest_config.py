POST_HARVEST_DB = {
    "tomato": {
        "max_temp": 25.0,
        "max_humidity": 80.0,
        "advice_high_temp": "phAdvTomatoTemp",
        "advice_high_hum": "phAdvTomatoHum",
        "base_risk": 0.15,
        "base_loss": 5.0
    },
    "potato": {
        "max_temp": 20.0,
        "max_humidity": 75.0,
        "advice_high_temp": "phAdvPotatoTemp",
        "advice_high_hum": "phAdvPotatoHum",
        "base_risk": 0.1,
        "base_loss": 3.0
    },
    "onion": {
        "max_temp": 30.0,
        "max_humidity": 65.0, # Needs it dry
        "advice_high_temp": "phAdvOnionTemp",
        "advice_high_hum": "phAdvOnionHum",
        "base_risk": 0.1,
        "base_loss": 4.0
    },
    "wheat": {
        "max_temp": 35.0,
        "max_humidity": 14.0, # Grain moisture threshold
        "advice_high_temp": "phAdvWheatTemp",
        "advice_high_hum": "phAdvWheatHum",
        "base_risk": 0.05,
        "base_loss": 1.0
    },
    "rice": {
        "max_temp": 35.0,
        "max_humidity": 14.0,
        "advice_high_temp": "phAdvRiceTemp",
        "advice_high_hum": "phAdvRiceHum",
        "base_risk": 0.05,
        "base_loss": 1.0
    }
}
