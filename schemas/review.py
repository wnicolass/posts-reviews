from pydantic import BaseModel
from decimal import Decimal as dec

class ReviewBase(BaseModel):
    rating: dec
    content: str
    reviewer_id: int
    post_id: int

class ReviewResult(ReviewBase):
    id: int