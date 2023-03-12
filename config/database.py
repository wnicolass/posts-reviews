import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())

engine = create_engine(url = os.getenv("CONNECTION_STRING"))
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

def create_metadata():
    import models.__all_models
    
    Base.metadata.drop_all(bind=engine)  
    Base.metadata.create_all(bind=engine)