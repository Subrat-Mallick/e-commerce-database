from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.database import get_database_url

# Create an engine for PostgreSQL
DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define your SQL database models here using SQLAlchemy's ORM
# Example:
# from app.models.customer import Customer
# from app.models.product import Product

# Add your SQL database utility functions here
# Example:
# def get_customer_by_id(session, customer_id):
#     return session.query(Customer).filter(Customer.id == customer_id).first()
