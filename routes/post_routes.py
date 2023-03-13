from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from schemas.post import PostBase, PostResult
from utils.db_session import get_db_session
from services import post_service

router = APIRouter()

@router.post('/posts', response_model = PostResult)
async def create_post(post: PostBase, session: Session = Depends(get_db_session)):
    inserted_data = post_service.create_post(post, session)
    if not inserted_data:
        return 'something went wrong'
    return inserted_data

@router.get('/posts')
async def get_posts() -> List[PostResult]:
    dummy_data = [
        {
        "id": 1,
        "title": 'dummy title',
        "summary": 'dummy summary',
        "content": 'dummy content'
        },
        {
        "id": 2,
        "title": 'dummy title 2',
        "summary": 'dummy summary 2',
        "content": 'dummy content 2'
        }
    ]
    return dummy_data