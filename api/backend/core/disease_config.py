# Mapping of disease ID to its details
DISEASE_DB = {
    "powdery_mildew": {
        "name": "Powdery Mildew",
        "treatment": "Apply sulfur-based fungicides or neem oil.",
        "prevention": "Ensure good air circulation, avoid overhead watering.",
        "cost_estimate": 800.0 # INR
    },
    "fusarium_wilt": {
        "name": "Fusarium Wilt",
        "treatment": "Remove and destroy infected plants. Fungicides are generally ineffective once infected.",
        "prevention": "Plant resistant varieties, practice crop rotation.",
        "cost_estimate": 300.0
    },
    "spider_mites": {
        "name": "Spider Mites",
        "treatment": "Apply acaricides or horticultural oils. Introduce predatory mites.",
        "prevention": "Maintain adequate moisture; dry conditions favor mites.",
        "cost_estimate": 1200.0
    },
    "caterpillars": {
        "name": "Caterpillars / Pests",
        "treatment": "Apply BT (Bacillus thuringiensis) or spinosad.",
        "prevention": "Use row covers, manually pick off large pests.",
        "cost_estimate": 600.0
    },
    "mosaic_virus": {
        "name": "Mosaic Virus",
        "treatment": "No cure. Destroy infected plants immediately.",
        "prevention": "Control aphids (virus vectors), use virus-free seeds.",
        "cost_estimate": 200.0
    },
    "unknown": {
        "name": "Unknown Issue",
        "treatment": "Consult a local agricultural extension officer.",
        "prevention": "Maintain general field hygiene.",
        "cost_estimate": 0.0
    }
}

# Symptom to disease mapping (first match wins for simplicity)
SYMPTOM_DISEASE_MAP = {
    "white_powdery": "powdery_mildew",
    "wilting_leaves": "fusarium_wilt",
    "webs_on_leaves": "spider_mites",
    "holes_in_leaves": "caterpillars",
    "yellow_mosaic": "mosaic_virus"
}
