from typing import List
from fastapi import APIRouter, HTTPException, Request, status, Depends, responses
from sqlalchemy.orm import Session
from schemas.review import ReviewBase, ReviewResult
from common.db_session import get_db_session
from services import review_service, post_service
from common.viewmodel import ViewModel
from common.utils import form_field_as_str
from decimal import Decimal as dec
from fastapi_chameleon import template

router = APIRouter()

@router.post("/reviews", status_code = status.HTTP_201_CREATED)
@template(template_file = "home/post_details.pt")
async def create_review(request: Request, session: Session = Depends(get_db_session)) -> ViewModel:
    vm = await create_review_viewmodel(request, session)

    if vm.error:
        return vm

    response = responses.RedirectResponse(url = f'/posts/{vm.post_id}', status_code = status.HTTP_302_FOUND)
    return response

async def create_review_viewmodel(request: Request, session: Session = Depends(get_db_session)) -> ViewModel:
    form_data = await request.form()

    vm = ViewModel(
        rating = dec(form_field_as_str(form_data, 'rating')),
        content = form_field_as_str(form_data, 'content'),
        post_id = int(form_field_as_str(form_data, 'post_id'))
    )

    if vm.rating < 0:
        vm.error, vm.error_msg =  True, "Rating cannot be negative."
    elif vm.rating > 5:
        vm.error, vm.error_msg =  True, "Rating cannot be greater than 5."
    elif not vm.content.strip():
        vm.error, vm.error_msg =  True, "Review content cannot be empty."

    if not vm.error:
        review_service.create_review(session, ReviewBase(
            rating = vm.rating,
            content = vm.content
        ), vm.post_id)
    else:
        current_post = post_service.get_post_by_id(session, vm.post_id)
        vm.post = current_post
        vm.total_reviews = len(current_post.related_reviews)
        vm.reviews = current_post.related_reviews

    return vm

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