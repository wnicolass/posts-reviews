from fastapi import APIRouter
from schemas.review import ReviewBase, ReviewResult

router = APIRouter()

@router.post("/reviews/{post_id}")
async def create_review(review: ReviewBase, post_id: int) -> ReviewResult:
    dummy_review = {
        "id": 1,
        "reviewer_id": review.reviewer_id,
        "rating": review.rating,
        "content": review.content
    }
    return dummy_review
