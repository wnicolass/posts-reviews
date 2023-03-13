from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    summary: str | None = None
    content: str

    class Config:
        orm_mode = True
    
class PostResult(PostBase):
    id: int
    created_at: datetime
