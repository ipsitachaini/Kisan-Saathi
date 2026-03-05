from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
from backend.core.config import settings

# Serverless connection settings
connect_args = {}
if "sqlite" not in settings.DATABASE_URL:
    connect_args = {"connect_timeout": 10}

engine = create_engine(
    settings.DATABASE_URL,
    poolclass=NullPool,
    connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
