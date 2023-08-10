# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

# SQLAlchemy configurations
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = DeclarativeBase()

# MongoDB configurations
MONGODB_URL = settings.mongodb_url
MONGODB_DATABASE_NAME = settings.mongodb_database_name
