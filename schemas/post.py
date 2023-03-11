from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    summary: str | None = None
    content: str
    
class PostResult(PostBase):
    id: int
