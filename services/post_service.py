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

def get_post_by_id(session: Session, id: int) -> model.Post:
    return session.query(model.Post).filter(model.Post.id == id).one_or_none()

def update_post(session: Session, post_to_update: model.Post, new_post: PostBase) -> model.Post:
    post_to_update.title = new_post.title
    post_to_update.summary = new_post.summary
    post_to_update.content = new_post.content

    session.commit()

    return post_to_update

def delete_post(session: Session, post: model.Post) -> None:
    session.delete(post)
    session.commit()