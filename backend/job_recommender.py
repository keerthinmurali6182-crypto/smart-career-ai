from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample job database (we will later connect real jobs API)
JOBS = [
    {
        "title": "Python Developer",
        "description": "Looking for Python developer with Flask, SQL and AWS experience"
    },
    {
        "title": "Data Scientist",
        "description": "Need ML engineer with Python, machine learning, deep learning and statistics"
    },
    {
        "title": "Frontend Developer",
        "description": "React, JavaScript, HTML, CSS developer needed"
    },
    {
        "title": "DevOps Engineer",
        "description": "Docker, Kubernetes, AWS, CI/CD pipelines experience required"
    }
]


def recommend_jobs(resume_text, top_k=3):
    results = []

    for job in JOBS:
        documents = [resume_text, job["description"]]

        tfidf = TfidfVectorizer(stop_words="english")
        matrix = tfidf.fit_transform(documents)

        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        score = round(score * 100, 2)

        results.append({
            "title": job["title"],
            "match_score": score
        })

    # sort best matches
    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return results[:top_k]