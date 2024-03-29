from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship
from config.database import Base
from models.review import Review

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(50), nullable = False)
    summary = Column(String(50), nullable = False)
    content = Column(String(255), nullable = False)
    created_at = Column(DateTime, default = datetime.now())

    related_reviews = relationship('Review', back_populates = 'post', cascade = 'delete')