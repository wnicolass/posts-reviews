from sqlalchemy.orm import Session
from typing import List
import models.review as model
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

def get_all_reviews(session: Session, post_id: int) -> List[model.Review]:
    return session.query(model.Review).where(model.Review.post_id == post_id).all()

def get_review_by_id(session: Session, review_id: int) -> model.Review:
    return session.query(model.Review).filter(model.Review.id == review_id).one_or_none()

def update_review(session: Session, review_id: int, new_data: ReviewBase) -> model.Review:
    db_review = get_review_by_id(session, review_id)
    db_review.rating = new_data.rating
    db_review.content = new_data.content
    
    session.commit()
    
    return db_review

def delete_review(session: Session, review_id) -> None:
    review_to_delete = get_post_by_id(session, review_id)
    session.delete(review_to_delete)
    session.commit()
