from fastapi import APIRouter
from services.feedback_ai import generate_feedback

router = APIRouter()


@router.post("/generate-feedback")
async def feedback(data: dict):

    result = generate_feedback(
        data.get("score"),
        data.get("skill_gap")
    )

    return {
        "feedback": result
    }