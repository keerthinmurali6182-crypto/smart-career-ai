from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow all origins (safe for dev + Vercel frontend)
CORS(app, resources={r"/*": {"origins": "*"}})

# -----------------------------
# SIMPLE SKILL DATABASE
# -----------------------------
SKILLS_DB = [
    "python", "flask", "django", "machine learning",
    "deep learning", "sql", "java", "c++",
    "html", "css", "javascript", "react",
    "aws", "docker", "kubernetes"
]

# -----------------------------
# JOB DATABASE
# -----------------------------
JOBS = [
    {
        "title": "Python Developer",
        "description": "python flask sql aws backend development"
    },
    {
        "title": "Data Scientist",
        "description": "python machine learning deep learning statistics sql"
    },
    {
        "title": "Frontend Developer",
        "description": "html css javascript react ui frontend"
    },
    {
        "title": "DevOps Engineer",
        "description": "docker kubernetes aws ci cd devops"
    }
]

# -----------------------------
# SKILL EXTRACTION
# -----------------------------
def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]


# -----------------------------
# ATS SCORE LOGIC
# -----------------------------
def calculate_ats(resume, job):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)

    if not job_skills:
        return 0

    matched = set(resume_skills) & set(job_skills)
    score = (len(matched) / len(job_skills)) * 100

    return round(score, 2)


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "🚀 Smart Career AI Running"
    })


# -----------------------------
# ATS SCORE API
# -----------------------------
@app.route("/resume-score", methods=["POST"])
def resume_score():
    data = request.get_json()

    resume = data.get("resume", "")
    job_description = data.get("job_description", "")

    if not resume or not job_description:
        return jsonify({"error": "resume and job_description required"}), 400

    score = calculate_ats(resume, job_description)
    matched_skills = extract_skills(resume)

    return jsonify({
        "ats_score": score,
        "matched_skills": matched_skills,
        "message": "ATS analysis complete"
    })


# -----------------------------
# JOB RECOMMENDATION API
# -----------------------------
@app.route("/recommend-jobs", methods=["POST"])
def recommend_jobs():
    data = request.get_json()
    resume = data.get("resume", "")

    results = []

    for job in JOBS:
        score = calculate_ats(resume, job["description"])
        results.append({
            "title": job["title"],
            "match_score": score
        })

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return jsonify({
        "recommended_jobs": results,
        "message": "Job recommendations generated"
    })


# -----------------------------
# SKILL GAP ANALYSIS API
# -----------------------------
@app.route("/skill-gap", methods=["POST"])
def skill_gap():
    data = request.get_json()
    resume = data.get("resume", "")

    resume_skills = extract_skills(resume)

    results = []

    for job in JOBS:
        job_skills = extract_skills(job["description"])

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        score = (len(matched) / (len(job_skills) + 1)) * 100

        results.append({
            "job_title": job["title"],
            "match_score": round(score, 2),
            "matched_skills": matched,
            "missing_skills": missing
        })

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return jsonify({
        "skill_gap_analysis": results,
        "message": "Skill gap analysis completed"
    })


# -----------------------------
# RUN SERVER (RENDER SAFE)
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)