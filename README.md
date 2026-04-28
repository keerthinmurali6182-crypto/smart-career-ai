# 🚀 Smart Career AI

An AI-powered web application that analyzes resumes against job descriptions and identifies missing skills.

---

## 🌐 Live Demo

Backend API:  
👉 https://smart-career-ai.onrender.com  

---

## 🧠 Features

- 📄 Upload Resume (PDF)
- 🎯 Match Score Calculation
- 🔍 Missing Skills Detection
- ⚡ Fast API Response
- 🌐 Deployed Backend

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **ML/NLP:** Scikit-learn  
- **PDF Parsing:** PyPDF2  
- **Frontend:** HTML, JavaScript  
- **Deployment:** Render  

---

## 📦 API Endpoints

### 🔹 GET /

Check if API is running

**Response:**
```md
```json
{
  "status": "API is running"
}

```json
{
  "status": "API is running"
}

## 🔹 POST /analyze

Analyze resume vs job description

**Request:**
- resume → PDF file  
- job_desc → text input  

---

**Response:**
```json
{
  "match_score": 75,
  "missing_skills": ["docker", "kubernetes"]
}
