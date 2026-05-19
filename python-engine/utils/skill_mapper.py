SKILL_ALIASES = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c": "C",
    "c++": "C++",
    "cpp": "C++",
    "c#": "C#",
    "golang": "Go",
    "go": "Go",
    "ruby": "Ruby",
    "php": "PHP",
    "react": "React",
    "reactjs": "React",
    "react.js": "React",
    "nextjs": "Next.js",
    "next.js": "Next.js",
    "vue": "Vue.js",
    "vuejs": "Vue.js",
    "angular": "Angular",
    "html": "HTML",
    "css": "CSS",
    "tailwind": "Tailwind CSS",
    "tailwindcss": "Tailwind CSS",
    "redux": "Redux",
    "nodejs": "Node.js",
    "node js": "Node.js",
    "node.js": "Node.js",
    "express": "Express.js",
    "expressjs": "Express.js",
    "express.js": "Express.js",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "spring": "Spring Boot",
    "spring boot": "Spring Boot",
    "mongodb": "MongoDB",
    "mongo": "MongoDB",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL",
    "sqlite": "SQLite",
    "redis": "Redis",
    "oracle": "OracleDB",
    "aws": "AWS",
    "amazon web services": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
    "google cloud": "GCP",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "k8s": "Kubernetes",
    "terraform": "Terraform",
    "jenkins": "Jenkins",
    "github actions": "GitHub Actions",
    "gitlab ci": "GitLab CI",
    "ansible": "Ansible",
    "linux": "Linux",
    "nginx": "NGINX",
    "git": "Git",
    "github": "GitHub",
    "bitbucket": "Bitbucket",
    "jira": "Jira",
    "postman": "Postman",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit learn": "Scikit-learn",
    "jwt": "JWT",
    "oauth": "OAuth",
    "authentication": "Authentication",
    "authorization": "Authorization"
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