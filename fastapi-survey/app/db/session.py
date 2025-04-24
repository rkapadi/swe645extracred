# app/db/session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
import logging

# Amazon RDS MySQL connection
DATABASE_URL = "mysql+mysqlconnector://admin:masterpassword!23@fastapi-db.c1ogbrnwz4yy.us-east-1.rds.amazonaws.com:3306/fastapi-db"
# DATABASE_URL = "mysql+mysqlconnector://admin:survey-db123456@database-1.cxzzxwkayrzc.us-east-1.rds.amazonaws.com:3306/survey_db_aws"

# Create engine
engine = create_engine(DATABASE_URL, pool_recycle=3600, pool_pre_ping=True)

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Enable logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
