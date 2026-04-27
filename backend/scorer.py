from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume, job):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume, job])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

def missing_skills(resume, job):
    resume_words = set(resume.split())
    job_words = set(job.split())

    missing = job_words - resume_words
    return list(missing)[:10]