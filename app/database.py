from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(db_url)

# Create a session factory
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()