from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from schemas.post import PostBase, PostResult
from utils.db_session import get_db_session
from services import post_service

router = APIRouter()

@router.post('/posts', response_model = PostResult, status_code = status.HTTP_201_CREATED)
async def create_post(post: PostBase, session: Session = Depends(get_db_session)):
    inserted_data = post_service.create_post(post, session)
    if not inserted_data:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail = {'error': 'Something went wrong while connecting to the database.'}
        )
    return inserted_data

@router.get('/posts', status_code = status.HTTP_200_OK)
async def get_posts(session: Session = Depends(get_db_session)) -> List[PostResult]:
    posts = post_service.get_posts(session)
    return posts

@router.put('/posts/{post_id}', response_model = PostResult, status_code = status.HTTP_200_OK)
async def update_post(post_id: int, new_post_data: PostBase, session: Session = Depends(get_db_session)):
    if not post_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = {'error': 'Missing id!'}
        )

    post = post_service.get_post_by_id(session, post_id)

    if not post:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = {'error': 'Post does not exist!'}
        )
    
    updated_post = post_service.update_post(session, post, new_post_data)

    return updated_post