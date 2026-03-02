# Mapping for crop recommendations based on conditions
# In reality, this would be a ML model or complex ruleset.
# For simplicity and configuration, we define a list of possible crops and conditions.
CROP_DB = [
    {
        "crop": "Wheat",
        "soil": ["red", "black", "clay"],
        "season": ["rabi"],
        "water": ["medium", "high"],
        "days_to_harvest": "120-150 Days",
        "expected_profit_per_acre": 25000.0,
        "advice_key": "cropAdvWheat"
    },
    {
        "crop": "Rice",
        "soil": ["clay", "black"],
        "season": ["kharif"],
        "water": ["high"],
        "days_to_harvest": "130-160 Days",
        "expected_profit_per_acre": 35000.0,
        "advice_key": "cropAdvRice"
    },
    {
        "crop": "Tomato",
        "soil": ["red", "black", "sandy"],
        "season": ["kharif", "rabi", "zaid"],
        "water": ["medium"],
        "days_to_harvest": "70-90 Days",
        "expected_profit_per_acre": 45000.0,
        "advice_key": "cropAdvTomato"
    },
    {
        "crop": "Onion",
        "soil": ["red", "sandy"],
        "season": ["rabi", "zaid"],
        "water": ["low", "medium"],
        "days_to_harvest": "100-120 Days",
        "expected_profit_per_acre": 50000.0,
        "advice_key": "cropAdvOnion"
    },
    {
        "crop": "Millets",
        "soil": ["red", "sandy", "black", "clay"],
        "season": ["kharif", "rabi"],
        "water": ["low"],
        "days_to_harvest": "80-100 Days",
        "expected_profit_per_acre": 15000.0,
        "advice_key": "cropAdvMillets"
    },
    {
        "crop": "Groundnut",
        "soil": ["sandy", "red"],
        "season": ["kharif", "rabi"],
        "water": ["low", "medium"],
        "days_to_harvest": "90-120 Days",
        "expected_profit_per_acre": 28000.0,
        "advice_key": "cropAdvGroundnut"
    }
]
