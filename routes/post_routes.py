from fastapi import APIRouter
from schemas.post import PostBase, PostResult
from typing import List

router = APIRouter()

@router.post('/posts')
async def create_post(post: PostBase) -> PostResult:
    dummy_data = {
        "id": 1,
        "title": post.title,
        "summary": post.summary,
        "content": post.content
    }
    return dummy_data

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