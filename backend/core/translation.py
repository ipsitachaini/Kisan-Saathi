import json
from pathlib import Path

LOCALES_DIR = Path(__file__).parent.parent.parent / "frontend" / "locales"
_translations = {}

def _load_translations():
    if _translations:
        return
    for lang in ["en", "hi", "or", "te", "ta", "bn"]:
        p = LOCALES_DIR / f"{lang}.json"
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                try:
                    _translations[lang] = json.load(f)
                except Exception:
                    _translations[lang] = {}

def translate(key: str, lang: str = "en", **kwargs) -> str:
    _load_translations()
    
    if lang not in _translations:
        lang = "en"
        
    table = _translations.get(lang, {})
    text = table.get(key)
    
    if not text:
        text = _translations.get("en", {}).get(key, key)
        
    for k, v in kwargs.items():
        text = text.replace(f"{{{k}}}", str(v))
        
    return text
