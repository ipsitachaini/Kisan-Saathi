from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    language = Column(String, default="en")
    created_at = Column(DateTime, default=datetime.utcnow)

    post_harvest_records = relationship("PostHarvestRecord", back_populates="owner")
    leaf_scans = relationship("LeafScanRecord", back_populates="owner")
    chats = relationship("ChatLog", back_populates="owner")
    yield_predictions = relationship("YieldPrediction", back_populates="owner")
    budget_records = relationship("BudgetRecord", back_populates="owner")
    fertilizer_reports = relationship("FertilizerReport", back_populates="owner")
    disease_reports = relationship("DiseaseReport", back_populates="owner")
    crop_recommendations = relationship("CropRecommendation", back_populates="owner")
    market_logs = relationship("MarketLog", back_populates="owner")

class YieldPrediction(Base):
    __tablename__ = "yield_predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    crop_name = Column(String, index=True)
    land_size = Column(Float) # in acres
    soil_quality = Column(String) # Good / Medium / Poor
    irrigation_availability = Column(Boolean)
    rainfall_level = Column(String)
    
    expected_yield = Column(Float) # in quintals
    expected_revenue = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="yield_predictions")

class BudgetRecord(Base):
    __tablename__ = "budget_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_budget = Column(Float)
    land_size = Column(Float)
    crop = Column(String)
    
    labour_cost = Column(Float)
    machine_cost = Column(Float)
    diesel_cost = Column(Float)
    seed_cost = Column(Float)
    fertilizer_cost = Column(Float)
    pesticide_cost = Column(Float)
    
    estimated_cost = Column(Float)
    remaining_budget = Column(Float)
    is_sufficient = Column(Boolean)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="budget_records")

class FertilizerReport(Base):
    __tablename__ = "fertilizer_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    input_type = Column(String) # "NPK" or "SYMPTOMS"
    n_value = Column(Float, nullable=True)
    p_value = Column(Float, nullable=True)
    k_value = Column(Float, nullable=True)
    symptoms = Column(String, nullable=True) # comma separated
    
    deficiency_detected = Column(String)
    fertilizer_name = Column(String)
    quantity_per_acre = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="fertilizer_reports")

class DiseaseReport(Base):
    __tablename__ = "disease_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symptoms = Column(String) # comma separated
    
    possible_issue = Column(String)
    treatment = Column(Text)
    prevention = Column(Text)
    cost_estimate = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="disease_reports")

class CropRecommendation(Base):
    __tablename__ = "crop_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    state = Column(String)
    city = Column(String)
    soil_type = Column(String)
    rainfall = Column(String)
    budget = Column(Float)
    
    top_crops = Column(Text) # JSON string of top 3 crops
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="crop_recommendations")

class MarketLog(Base):
    __tablename__ = "market_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    crop = Column(String)
    city = Column(String)
    state = Column(String)
    
    current_price = Column(Float)
    trend = Column(String) # UP, DOWN, STABLE
    suggestion = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="market_logs")

class PostHarvestRecord(Base):
    __tablename__ = "post_harvest_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    crop_type = Column(String, index=True)
    storage_method = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    storage_duration = Column(Integer) # in days
    location = Column(String)
    
    spoilage_risk_score = Column(Float)
    loss_percentage = Column(Float)
    storage_advice = Column(Text)
    sell_suggestion = Column(String) # e.g. "SELL", "HOLD"
    
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="post_harvest_records")

class LeafScanRecord(Base):
    __tablename__ = "leaf_scan_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    image_url = Column(String) # path to stored image
    disease_prediction = Column(String)
    confidence_score = Column(Float)
    scan_date = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="leaf_scans")

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message_text = Column(Text)
    is_bot = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="chats")

class WeatherCache(Base):
    __tablename__ = "weather_cache"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, unique=True, index=True)
    data = Column(Text) # JSON string representation
    last_updated = Column(DateTime, default=datetime.utcnow)
