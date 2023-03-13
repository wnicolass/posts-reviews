from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    DECIMAL,
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.database import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key = True, autoincrement = True)
    rating = Column(DECIMAL(3, 1), nullable = False)
    content = Column(String(255), nullable = False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable = False)
    created_at = Column(DateTime, default = datetime.now())

    post = relationship('Post', back_populates = 'related_reviews')