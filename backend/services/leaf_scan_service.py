from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
from backend.db.models import User, LeafScanRecord
import shutil
import uuid
import os
import random

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def process_leaf_scan(db: Session, user: User, file: UploadFile) -> LeafScanRecord:
    # 1. Validate file
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
        
    # 2. Save file locally securely
    file_ext = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Relative URL to serve the image later
    image_url = f"/static/{unique_filename}"
    
    # 3. Mock ML Prediction Logic
    # In reality, this would pass the image buffer to an ML service (e.g., PyTorch model)
    possible_diseases = [
        "Healthy",
        "Early Blight",
        "Late Blight",
        "Leaf Mold",
        "Target Spot",
        "Spider Mites",
        "Tomato Yellow Leaf Curl Virus"
    ]
    
    prediction = random.choice(possible_diseases)
    confidence = random.uniform(0.70, 0.99)
    
    if prediction == "Healthy":
        confidence = random.uniform(0.85, 0.99)
        
    # 4. Save record to DB
    record = LeafScanRecord(
        user_id=user.id,
        image_url=image_url,
        disease_prediction=prediction,
        confidence_score=round(confidence, 2)
    )
    
    db.add(record)
    db.commit()
    db.refresh(record)
    
    return record
