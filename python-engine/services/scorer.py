from utils.cosine import cosine_similarity_score



def calculate_skill_score(parsed_job, skill_gap):

    total_skills = len(parsed_job.get("skills", []))

    matched = len(skill_gap.get("matched_skills", []))

    if total_skills == 0:
        return 0

    return (matched / total_skills) * 100



def calculate_experience_score(parsed_job, resume_data):

    required = parsed_job.get("experienceYears", 0)

    candidate = resume_data.get("experienceYears", 0)

    if candidate >= required:
        return 100

    if required == 0:
        return 100

    return (candidate / required) * 100



def calculate_education_score(parsed_job, resume_data):

    job_education = set(parsed_job.get("education", []))

    candidate_education = set(resume_data.get("education", []))

    if len(job_education.intersection(candidate_education)) > 0:
        return 100

    return 0



def calculate_semantic_score(parsed_job, resume_data):

    job_embedding = parsed_job.get("embedding", [])

    resume_embedding = resume_data.get("embedding", [])

    similarity = cosine_similarity_score(
        job_embedding,
        resume_embedding
    )

    return similarity * 100



def calculate_score(parsed_job, resume_data, skill_gap):
    skill_score = calculate_skill_score(
        parsed_job,
        skill_gap
    )

    experience_score = calculate_experience_score(
        parsed_job,
        resume_data
    )

    education_score = calculate_education_score(
        parsed_job,
        resume_data
    )

    semantic_score = calculate_semantic_score(
        parsed_job,
        resume_data
    )

    final_score = (
        (skill_score * 0.4) +
        (experience_score * 0.2) +
        (education_score * 0.1) +
        (semantic_score * 0.3)
    )

    return round(final_score)