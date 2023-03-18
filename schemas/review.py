from pydantic import BaseModel
from decimal import Decimal as dec
from datetime import datetime

class ReviewBase(BaseModel):
    rating: dec
    content: str

    class Config:
        orm_mode = True

class ReviewResult(ReviewBase):
    id: int
    post_id: int
    created_at: datetime