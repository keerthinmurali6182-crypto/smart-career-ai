# 🚀 Smart Career AI

An AI-powered Resume Analyzer SaaS that evaluates resumes against job descriptions, calculates ATS score, recommends jobs, and identifies skill gaps.

---

## 🌐 Live Backend

https://smart-career-ai.onrender.com

---

## 🧠 Features

- 📄 Resume analysis (paste-based input)
- 🎯 ATS Score calculation
- 🔍 Skill extraction from resume
- 💼 Job recommendation system
- 🧠 Skill gap analysis
- ⚡ Fast Flask REST API
- 🌍 CORS-enabled for frontend integration

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask-CORS

### Frontend
- React.js
- Axios

### Deployment
- Render (Backend)
- Local / Vercel (Frontend)

---

## 📂 Project Structure
backend/
│ app.py
│ requirements.txt
│
frontend/
│ src/
│ App.js
│ package.json


---

## 🚀 API Endpoints

### 🔹 Home
```

GET /

```

Response:
```json
{
  "message": "🚀 Smart Career AI Running"
}


🔹 ATS Score
POST /resume-score

Request:

{
  "resume": "python flask sql machine learning",
  "job_description": "python flask aws backend development"
}

Response:

{
  "ats_score": 85.5,
  "matched_skills": ["python", "flask", "sql"]
}

🔹 Job Recommendations
POST /recommend-jobs


🔹 Skill Gap Analysis
POST /skill-gap

💻 How to Run Locally
Backend
cd backend
pip install -r requirements.txt
python app.py

Runs on:
http://localhost:5000

Frontend
cd frontend
npm install
npm start

Runs on:
http://localhost:3000

🔗 Frontend Configuration

Make sure your React frontend uses:
const API = "https://smart-career-ai.onrender.com";

📊 Example Output
ATS Score: 90%
Matched Skills: python, flask, sql, react, aws, docker

🚀 Future Improvements
🔐 Login system
💳 Stripe payments
📄 PDF resume upload
🤖 AI-based scoring (NLP/LLM)
📊 Dashboard analytics
🌐 Full SaaS deployment

##👨‍💻 Author
Built using Flask + React 🚀
