from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_parser import extract_text_from_pdf
from scorer import compute_similarity, missing_skills

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "🚀 Smart Career AI Running"})

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    file = request.files['resume']
    job_desc = request.form.get('job_desc', '')

    resume_text = extract_text_from_pdf(file)
    score = compute_similarity(resume_text, job_desc)
    gaps = missing_skills(resume_text, job_desc)

    return jsonify({
        "match_score": score,
        "missing_skills": gaps
    })

# IMPORTANT for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)