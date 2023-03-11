from pydantic import BaseModel
from decimal import Decimal as dec

class ReviewBase(BaseModel):
    reviewer_id: int
    rating: dec
    content: str

class ReviewResult(ReviewBase):
    id: int