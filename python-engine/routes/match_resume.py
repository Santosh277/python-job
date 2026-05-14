from fastapi import APIRouter
from services.resume_extractor import extract_resume_data
from services.matcher import build_skill_gap
from services.scorer import calculate_score

router = APIRouter()


@router.post("/match-resume")
async def match_resume(data: dict):

    parsed_job = data.get("parsed_job")
    resume_url = data.get("resume_url")

    resume_data = extract_resume_data(resume_url)

    skill_gap = build_skill_gap(
        parsed_job,
        resume_data
    )

    score = calculate_score(
        parsed_job,
        resume_data,
        skill_gap
    )

    return {
        "score": score,
        "skill_gap": skill_gap
    }