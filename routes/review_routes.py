from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas.review import ReviewBase, ReviewResult
from utils.db_session import get_db_session
from services import review_service, post_service

router = APIRouter()

@router.post("/reviews/{post_id}", status_code = status.HTTP_201_CREATED)
async def create_review(review: ReviewBase, post_id: int, session: Session = Depends(get_db_session)) -> ReviewResult:
    if not post_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = {'error': 'Missing id.'}
        )
    
    if not post_service.get_post_by_id(session, post_id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = {'error': f'Post with id {post_id} not found.'}
        )
    
    new_review = review_service.create_review(session, review, post_id)
    
    if not new_review:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail = {'error': 'Something went wrong while connecting to the database.'}
        )
    
    return new_review
