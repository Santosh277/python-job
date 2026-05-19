import os
from utils.downloader import download_resume
from utils.pdf_reader import read_pdf
from utils.docx_reader import read_docx
from utils.text_cleaner import clean_text
from utils.skill_mapper import extract_skills
from utils.experience_extractor import extract_experience
from services.embeddings import generate_embedding


EDUCATION_KEYWORDS = [
    "B.Tech",
    "B.E",
    "BE",
    "M.Tech",
    "M.E",
    "MCA",
    "BCA",
    "B.Sc",
    "M.Sc",
    "MBA",
    "PhD",
    "Diploma",
    "Bachelor",
    "Bachelor's",
    "Master",
    "Master's",
    "Bachelor of Technology",
    "Bachelor of Engineering",
    "Master of Technology",
    "Master of Engineering",
    "Bachelor of Computer Applications",
    "Master of Computer Applications",
    "Computer Science",
    "Computer Engineering",
    "Information Technology",
    "Electronics",
    "Electronics and Communication",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Data Science",
    "Artificial Intelligence",
    "Machine Learning",
    "Software Engineering"
]


def extract_education(text):
    found = []

    lower_text = text.lower()

    for edu in EDUCATION_KEYWORDS:
        if edu.lower() in lower_text:
            found.append(edu)

    return list(set(found))



def extract_resume_data(url):

    file_path = download_resume(url)

    if file_path.endswith(".pdf"):
        raw_text = read_pdf(file_path)

    elif file_path.endswith(".docx"):
        raw_text = read_docx(file_path)

    else:
        raise Exception("Unsupported resume format")

    cleaned = clean_text(raw_text)

    skills = extract_skills(cleaned)

    education = extract_education(cleaned)

    experience = extract_experience(cleaned)

    embedding = generate_embedding(cleaned)

    os.remove(file_path)

    return {
        "skills": skills,
        "education": education,
        "experienceYears": experience,
        "normalizedText": cleaned,
        "embedding": embedding
    }