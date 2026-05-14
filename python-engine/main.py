from fastapi import FastAPI
from routes.parse_job import router as parse_router
from routes.match_resume import router as match_router
from routes.generate_feedback import router as feedback_router

app = FastAPI()

app.include_router(parse_router)
app.include_router(match_router)
app.include_router(feedback_router)


@app.get("/")
def root():
    return {"message": "ATS Engine Running"}