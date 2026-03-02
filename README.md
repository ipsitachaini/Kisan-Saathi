# Kisan Saathi

**Smart Farming & Post-Harvest Assistant**

Kisan Saathi is a full-stack intelligence platform designed to empower farmers with actionable insights. It provides tools for weather tracking, leaf disease detection, and predicting post-harvest risks to minimize losses and maximize profits.

## Core Features
1. **Authentication**: Secure JWT-based registration and login system.
2. **Farmer Dashboard**: A unified view for weather updates, crop selection, and module shortcuts.
3. **Post-Harvest Intelligence**: 
   - Analyze storage combinations (crop type, temperature, duration).
   - Get spoilage risk scores, predicted loss percentages, and storage advice.
   - Intelligent "Sell vs. Hold" suggestions.
4. **Leaf Disease Detection**: Upload crop images to receive AI-powered disease predictions and confidence scores (AI integration ready).
5. **Chatbot Module**: Context-aware digital assistant for farming queries.
6. **Weather Integration**: Localized data caching for fast weather updates.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Frontend**: Vanilla HTML, CSS, JavaScript (Modular architecture)
- **Security**: JWT tokens, bcrypt hashed passwords.
- **Environment**: Configured using `pydantic-settings` via `.env`.

## Multilingual Support
Kisan Saathi is committed to regional accessibility. Our core tagline "Smart Farming & Post-Harvest Assistant" translates to:
- **Hindi (हिन्दी)**: स्मार्ट कृषि और फसल-पश्चात सहायक
- **Odia (ଓଡ଼ିଆ)**: ସ୍ମାର୍ଟ କୃଷି ଏବଂ ଅମଳ ପରବର୍ତ୍ତୀ ସହାୟକ
- **Telugu (తెలుగు)**: స్మార్ట్ వ్యవసాయం మరియు కోత అనంతర సహాయకుడు
- **Tamil (தமிழ்)**: ஸ்மார்ட் விவசாயம் மற்றும் அறுவடைக்கு பிந்தைய உதவியாளர்
- **Bengali (বাংলা)**: স্মার্ট কৃষি এবং ফসল পরবর্তী সহকারী

## Setup Instructions

### 1. Backend Setup
1. Navigate to the `backend/` directory.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI development server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend Setup
1. In a new terminal, navigate to the `frontend/` directory.
2. Start a simple HTTP server to serve the static files:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`.
