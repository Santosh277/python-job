from utils.skill_mapper import normalize_skill


def build_skill_gap(parsed_job, resume_data):

    job_skills = parsed_job.get("skills", [])
    resume_skills = resume_data.get("skills", [])

    normalized_job = set([
        normalize_skill(skill)
        for skill in job_skills
    ])

    normalized_resume = set([
        normalize_skill(skill)
        for skill in resume_skills
    ])

    matched = list(normalized_job.intersection(normalized_resume))

    missing = list(normalized_job.difference(normalized_resume))

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }