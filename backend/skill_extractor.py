import spacy

nlp = spacy.load("en_core_web_sm")

# simple skill database (we will improve later)
SKILL_DB = [
    "python", "flask", "django", "machine learning",
    "deep learning", "sql", "java", "c++",
    "html", "css", "javascript", "react",
    "aws", "docker"
]

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_DB:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))