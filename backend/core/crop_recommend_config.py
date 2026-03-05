# Mapping for crop recommendations based on conditions
# In reality, this would be a ML model or complex ruleset.
# For simplicity and configuration, we define a list of possible crops and conditions.
CROP_DB = [
    {
    "crop": "Wheat",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium",
        "high"
    ],
    "days_to_harvest": "120-150 Days",
    "expected_profit_per_acre": 25000.0,
    "advice_key": "cropAdvWheat"
},
    {
    "crop": "Rice",
    "soil": [
        "clay",
        "black"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "130-160 Days",
    "expected_profit_per_acre": 35000.0,
    "advice_key": "cropAdvRice"
},
    {
    "crop": "Tomato",
    "soil": [
        "red",
        "black",
        "sandy"
    ],
    "season": [
        "kharif",
        "rabi",
        "zaid"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "70-90 Days",
    "expected_profit_per_acre": 45000.0,
    "advice_key": "cropAdvTomato"
},
    {
    "crop": "Onion",
    "soil": [
        "red",
        "sandy"
    ],
    "season": [
        "rabi",
        "zaid"
    ],
    "water": [
        "low",
        "medium"
    ],
    "days_to_harvest": "100-120 Days",
    "expected_profit_per_acre": 50000.0,
    "advice_key": "cropAdvOnion"
},
    {
    "crop": "Millets",
    "soil": [
        "red",
        "sandy",
        "black",
        "clay"
    ],
    "season": [
        "kharif",
        "rabi"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "80-100 Days",
    "expected_profit_per_acre": 15000.0,
    "advice_key": "cropAdvMillets"
},
    {
    "crop": "Groundnut",
    "soil": [
        "sandy",
        "red"
    ],
    "season": [
        "kharif",
        "rabi"
    ],
    "water": [
        "low",
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 28000.0,
    "advice_key": "cropAdvGroundnut"
},
    {
    "crop": "Maize",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMaize"
},
    {
    "crop": "Bajra",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBajra"
},
    {
    "crop": "Jowar",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvJowar"
},
    {
    "crop": "Ragi",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvRagi"
},
    {
    "crop": "Barley",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBarley"
},
    {
    "crop": "Foxtail Millet",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvFoxtailmillet"
},
    {
    "crop": "Little Millet",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvLittlemillet"
},
    {
    "crop": "Kodo Millet",
    "soil": [
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvKodomillet"
},
    {
    "crop": "Arhar",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvArhar"
},
    {
    "crop": "Moong",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMoong"
},
    {
    "crop": "Urad",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvUrad"
},
    {
    "crop": "Masoor",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMasoor"
},
    {
    "crop": "Chana",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvChana"
},
    {
    "crop": "Rajma",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvRajma"
},
    {
    "crop": "Horse Gram",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvHorsegram"
},
    {
    "crop": "Lobia",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvLobia"
},
    {
    "crop": "Mustard",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMustard"
},
    {
    "crop": "Soybean",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvSoybean"
},
    {
    "crop": "Sunflower",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvSunflower"
},
    {
    "crop": "Sesame",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvSesame"
},
    {
    "crop": "Castor",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCastor"
},
    {
    "crop": "Linseed",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "low"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvLinseed"
},
    {
    "crop": "Potato",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvPotato"
},
    {
    "crop": "Brinjal",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBrinjal"
},
    {
    "crop": "Cabbage",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCabbage"
},
    {
    "crop": "Cauliflower",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCauliflower"
},
    {
    "crop": "Okra",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvOkra"
},
    {
    "crop": "Chilli",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvChilli"
},
    {
    "crop": "Capsicum",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCapsicum"
},
    {
    "crop": "Pumpkin",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvPumpkin"
},
    {
    "crop": "Bottle Gourd",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBottlegourd"
},
    {
    "crop": "Bitter Gourd",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBittergourd"
},
    {
    "crop": "Ridge Gourd",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvRidgegourd"
},
    {
    "crop": "Spinach",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvSpinach"
},
    {
    "crop": "Carrot",
    "soil": [
        "red",
        "sandy",
        "black"
    ],
    "season": [
        "rabi"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCarrot"
},
    {
    "crop": "Mango",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMango"
},
    {
    "crop": "Banana",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvBanana"
},
    {
    "crop": "Papaya",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvPapaya"
},
    {
    "crop": "Guava",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvGuava"
},
    {
    "crop": "Apple",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvApple"
},
    {
    "crop": "Pomegranate",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvPomegranate"
},
    {
    "crop": "Watermelon",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvWatermelon"
},
    {
    "crop": "Muskmelon",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "zaid"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvMuskmelon"
},
    {
    "crop": "Litchi",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvLitchi"
},
    {
    "crop": "Sugarcane",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvSugarcane"
},
    {
    "crop": "Turmeric",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvTurmeric"
},
    {
    "crop": "Cotton",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "medium"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCotton"
},
    {
    "crop": "Jute",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvJute"
},
    {
    "crop": "Tea",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvTea"
},
    {
    "crop": "Coffee",
    "soil": [
        "red",
        "black",
        "clay"
    ],
    "season": [
        "kharif"
    ],
    "water": [
        "high"
    ],
    "days_to_harvest": "90-120 Days",
    "expected_profit_per_acre": 20000.0,
    "advice_key": "cropAdvCoffee"
}
],
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
