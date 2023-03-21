from fastapi import APIRouter, Depends, Request, status, HTTPException, responses
from fastapi_chameleon import template
from typing import List
from sqlalchemy.orm import Session

from schemas.post import PostBase, PostResult
from common.db_session import get_db_session
from services import post_service
from common.viewmodel import ViewModel
from common.utils import form_field_as_str

router = APIRouter()

@router.get('/posts/new', status_code = status.HTTP_200_OK)
@template(template_file = 'home/new_post.pt')
async def new_post():
    return new_post_viewmodel()

def new_post_viewmodel():
    return ViewModel()

@router.post('/posts/new', status_code = status.HTTP_201_CREATED)
@template(template_file = 'home/new_post.pt')
async def create_post(request: Request, session: Session = Depends(get_db_session)):
    vm = await create_post_viewmodel(request, session)
    
    if vm.error:
        return vm

    response = responses.RedirectResponse(url = '/posts', status_code = status.HTTP_302_FOUND)
    return response

async def create_post_viewmodel(request: Request, session: Session = Depends(get_db_session)):
    form_data = await request.form()

    vm = ViewModel(
        title = form_field_as_str(form_data, 'title'),
        summary = form_field_as_str(form_data, 'summary'),
        content = form_field_as_str(form_data, 'content')
    )

    if len(vm.title.strip()) < 2:
        vm.error, vm.error_msg = True, "Title must has at least 2 characters."
    elif len(vm.content.strip()) < 5: 
        vm.error, vm.error_msg = True, "Content must has at least 5 characters."
    
    if not vm.error:
        post_service.create_post(PostBase(
            title = vm.title,
            summary = vm.content,
            content = vm.content
        ), session)
    
    return vm

@router.get('/posts', status_code = status.HTTP_200_OK)
@template(template_file = 'home/posts.pt')
async def get_posts(session: Session = Depends(get_db_session)) -> dict:
    return get_posts_viewmodel(session)

def get_posts_viewmodel(session: Session):
    posts = post_service.get_posts(session)

    vm = ViewModel(
        posts = posts, 
        total = len(posts)
    )

    return vm

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

@router.delete('/posts/{post_id}', status_code = status.HTTP_200_OK)
async def delete_post(post_id: int, session: Session = Depends(get_db_session)) -> None:
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
    
    post_service.delete_post(session, post)
    
    return {'message': 'Post deleted successfully.'}
