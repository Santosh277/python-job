from services.embeddings import generate_embedding
from utils.text_cleaner import clean_text
from utils.skill_mapper import extract_skills
from utils.experience_extractor import extract_experience

EDUCATION_KEYWORDS = [
    "B.Tech",
    "B.E",
    "MCA",
    "Bachelor",
    "Master",
    "Computer Science"
]


KEYWORDS = [
    "REST API",
    "Microservices",
    "Backend",
    "Cloud",
    "Distributed Systems"
]


def extract_education(text):
    found = []

    lower_text = text.lower()

    for edu in EDUCATION_KEYWORDS:
        if edu.lower() in lower_text:
            found.append(edu)

    return list(set(found))


def extract_keywords(text):
    found = []

    lower_text = text.lower()

    for keyword in KEYWORDS:
        if keyword.lower() in lower_text:
            found.append(keyword)

    return list(set(found))


def parse_job_description(data):

    title = data.get("title", "")
    description = data.get("description", "")
    requirements = data.get("requirements", [])

    combined_text = f'''
    {title}
    {description}
    {' '.join(requirements)}
    '''

    cleaned = clean_text(combined_text)

    skills = extract_skills(cleaned)

    keywords = extract_keywords(cleaned)

    education = extract_education(cleaned)

    experience = extract_experience(cleaned)

    embedding = generate_embedding(cleaned)

    return {
        "skills": skills,
        "keywords": keywords,
        "education": education,
        "normalizedText": cleaned,
        "experienceYears": experience,
        "embedding": embedding
    }