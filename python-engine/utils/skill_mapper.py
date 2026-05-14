SKILL_ALIASES = {
    "nodejs": "Node.js",
    "node js": "Node.js",
    "expressjs": "Express.js",
    "mongodb": "MongoDB",
    "mongo": "MongoDB",
    "reactjs": "React",
    "aws": "AWS",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "python": "Python",
    "java": "Java",
    "redis": "Redis"
}



def normalize_skill(skill):

    cleaned = skill.lower().strip()

    return SKILL_ALIASES.get(cleaned, skill)



def extract_skills(text):

    found = []

    lower_text = text.lower()

    for alias, original in SKILL_ALIASES.items():

        if alias in lower_text:
            found.append(original)

    return list(set(found))