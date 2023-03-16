from sqlalchemy.orm import Session
from typing import List
import models.post as model
from schemas.review import ReviewBase
from services.post_service import get_post_by_id

def create_review(session: Session, review_sch: ReviewBase, post_id: int) -> model.Review:
    db_review = model.Review(
        rating = review_sch.rating,
        content = review_sch.content,
        post_id = post_id
    )
    post = get_post_by_id(session, post_id)
    db_review.post = post
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review