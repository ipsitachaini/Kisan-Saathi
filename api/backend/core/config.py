from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Kisan Saathi API"
    API_V1_STR: str = "/api/v1"
    
    # Database (Fallback to a temporary writable directory to prevent Vercel crashes)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:////tmp/sql_app.db")
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-here-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
