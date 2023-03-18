from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas.review import ReviewBase, ReviewResult
from utils.db_session import get_db_session
from services import review_service, post_service
from models.review import Review

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

@router.get("/reviews/{post_id}", status_code = status.HTTP_200_OK)
async def get_reviews(post_id: int, session: Session = Depends(get_db_session)) -> List[ReviewResult]:
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
    
    post_reviews = review_service.get_all_reviews(session, post_id)
    return post_reviews

@router.patch("/reviews/{review_id}", status_code = status.HTTP_200_OK)
async def update_review(review_id: int, new_review: ReviewBase, session: Session = Depends(get_db_session)) -> ReviewResult:
    if not review_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = {'error': 'Missing id.'}
        )
    
    updated_review = review_service.update_review(session, review_id, new_review)
    return updated_review

@router.delete("/reviews/{review_id}", status_code = status.HTTP_200_OK)
async def delete_review(review_id: int, session: Session = Depends(get_db_session)) -> dict:
    if not review_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = {'error': 'Missing id.'}
        )
    
    review_service.delete_review(session, review_id)
    
    return {'message': 'Review deleted successfully.'}