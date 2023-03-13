from sqlalchemy.orm import Session

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
