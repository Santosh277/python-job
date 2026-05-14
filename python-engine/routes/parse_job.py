from fastapi import APIRouter
from services.jd_parser import parse_job_description

router = APIRouter()


@router.post("/parse-job")
async def parse_job(data: dict):
    result = parse_job_description(data)
    return result