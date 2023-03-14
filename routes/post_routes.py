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
            detail = {'error': 'Something went wrong! While connecting to the database.'}
        )
    return inserted_data

@router.get('/posts', status_code = status.HTTP_200_OK)
async def get_posts(session: Session = Depends(get_db_session)) -> List[PostResult]:
    posts = post_service.get_posts(session)
    return posts