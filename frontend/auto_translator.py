import json
import os
import sys
from googletrans import Translator
import time
import re

translator = Translator()

locales_dir = r"c:\Users\ipsit\OneDrive\Documents\New folder\smart-agri-platform\frontend\locales"
langs = {"hi": "hi", "or": "or", "te": "te", "ta": "ta", "bn": "bn", "en": "en"}

# The new manual format:
base_templates = {
    "en": {"disease_summary": "Based on the symptoms, we suspect {disease}. Treatment involves {treatment} with an estimated cost of ₹{cost}."},
    "hi": {"disease_summary": "लक्षणों के आधार पर, हमें {disease} का संदेह है। उपचार में ₹{cost} की अनुमानित लागत के साथ {treatment} शामिल है।"},
    "or": {"disease_summary": "ଲକ୍ଷଣ ଉପରେ ଭିତ୍ତି କରି ଆମେ {disease} ସନ୍ଦେହ କରୁଛୁ। ଚିକିତ୍ସାରେ ₹{cost} ଆନୁମାନିକ ଖର୍ଚ୍ଚ ସହିତ {treatment} ଅନ୍ତର୍ଭୁକ୍ତ।"},
    "te": {"disease_summary": "లక్షణాల ఆధారంగా, మేము {disease} అని అనుమానిస్తున్నాము. చికిత్సలో ₹{cost} అంచనా ఖర్చుతో {treatment} ఉంటుంది."},
    "ta": {"disease_summary": "அறிகுறிகளின் அடிப்படையில், இது {disease} என்று நாங்கள் சந்தேகிக்கிறோம். சிகிச்சைக்கு தோராயமாக ₹{cost} செலவில் {treatment} தேவைப்படும்."},
    "bn": {"disease_summary": "লক্ষণগুলির উপর ভিত্তি করে, আমরা {disease} সন্দেহ করছি। চিকিৎসায় ₹{cost} আনুমানিক খরচ সহ {treatment} জড়িত।"}
}

# Values that must be translated since they are passed dynamically into placeholders
english_values_to_translate = [
    # Diseases & Treatments
    "Powdery Mildew", "Apply sulfur-based fungicides or neem oil.",
    "Fusarium Wilt", "Remove and destroy infected plants. Fungicides are generally ineffective once infected.",
    "Spider Mites", "Apply acaricides or horticultural oils. Introduce predatory mites.",
    "Caterpillars / Pests", "Apply BT (Bacillus thuringiensis) or spinosad.",
    "Mosaic Virus", "No cure. Destroy infected plants immediately.",
    "Unknown Issue", "Consult a local agricultural extension officer.",
    
    # Fertilizer
    "Nitrogen (N) Deficiency", "Phosphorus (P) Deficiency", "Potassium (K) Deficiency", "Balanced",
    "Urea (46-0-0)", "DAP (18-46-0)", "MOP (0-0-60)", "NPK (19-19-19) or Compost",
    
    # Other dynamic vars if needed
]


def update_locales():
    for lang, l_code in langs.items():
        file_path = os.path.join(locales_dir, f"{lang}.json")
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Add template
        data.update(base_templates[lang])
        
        # Translate literal values
        if lang != "en":
            for val in english_values_to_translate:
                if val not in data:
                    try:
                        res = translator.translate(val, dest=l_code)
                        data[val] = res.text
                    except Exception as e:
                        print(f"Failed to translate {val} for {lang}: {e}")
                        data[val] = val
        else:
            for val in english_values_to_translate:
                if val not in data:
                    data[val] = val
                    
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_locales()
