# Mapping of common symptoms to their likely nutrient deficiency
SYMPTOM_DEFICIENCY_MAP = {
    "yellow_leaves": "Nitrogen (N) Deficiency",
    "weak_roots": "Phosphorus (P) Deficiency",
    "brown_edges": "Potassium (K) Deficiency",
    "stunted_growth": "Nitrogen (N) or Phosphorus (P) Deficiency",
    "purple_leaves": "Phosphorus (P) Deficiency",
    "curling_leaves": "Potassium (K) Deficiency"
}

# Recommendations based on deficiency
DEFICIENCY_RECOMMENDATION = {
    "Nitrogen (N) Deficiency": {
        "fertilizer_name": "Urea",
        "quantity_per_acre": 45.0 # kg
    },
    "Phosphorus (P) Deficiency": {
        "fertilizer_name": "DAP (Diammonium Phosphate)",
        "quantity_per_acre": 50.0 # kg
    },
    "Potassium (K) Deficiency": {
        "fertilizer_name": "MOP (Muriate of Potash)",
        "quantity_per_acre": 30.0 # kg
    },
    "Nitrogen (N) or Phosphorus (P) Deficiency": {
        "fertilizer_name": "NPK 19-19-19",
        "quantity_per_acre": 40.0 # kg
    },
    "Balanced": {
        "fertilizer_name": "Standard Compost / Manure",
        "quantity_per_acre": 1000.0 # kg
    }
}

# Thresholds for NPK mode (basic example)
# Below these values, it's considered deficient
NPK_THRESHOLDS = {
    "N": 30, # kg/ha equivalent or simple index
    "P": 15,
    "K": 20
}
