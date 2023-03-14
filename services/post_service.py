from sqlalchemy.orm import Session
from typing import List
import models.post as model
from schemas.post import PostBase

def create_post(post: PostBase, session: Session) -> model.Post:
    db_post = model.Post(
        title = post.title,
        summary = post.summary,
        content = post.summary
    )
    
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

def get_posts(session: Session) -> List[model.Post]:
    return session.query(model.Post).all()