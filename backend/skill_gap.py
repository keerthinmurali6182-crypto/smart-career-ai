from job_recommender import JOBS

# simple skill database (same as earlier)
SKILL_DB = [
    "python", "flask", "django", "machine learning",
    "deep learning", "sql", "java", "c++",
    "html", "css", "javascript", "react",
    "aws", "docker", "kubernetes"
]


def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILL_DB if skill in text_lower]


def skill_gap_analysis(resume_text):
    user_skills = extract_skills(resume_text)

    results = []

    for job in JOBS:
        job_skills = extract_skills(job["description"])

        missing = list(set(job_skills) - set(user_skills))
        matched = list(set(job_skills) & set(user_skills))

        results.append({
            "job_title": job["title"],
            "matched_skills": matched,
            "missing_skills": missing,
            "match_score": round((len(matched) / (len(job_skills) + 1)) * 100, 2)
        })

    # sort best match first
    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return results