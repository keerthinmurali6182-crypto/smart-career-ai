# 🚀 Smart Career AI

An AI-powered web application that analyzes resumes against job descriptions and identifies missing skills, along with a match score.

---

## 🌐 Live Demo

### Backend (Render)

👉 [https://smart-career-ai.onrender.com](https://smart-career-ai.onrender.com)

### Frontend (Vercel)

👉 [https://smart-career-3wj8yno4x-keerthinmurali6182-cryptos-projects.vercel.app](https://smart-career-3wj8yno4x-keerthinmurali6182-cryptos-projects.vercel.app)

---

## 🧠 Features

* 📄 Upload Resume (PDF)
* 🎯 Job Description Matching
* 📊 Match Score Calculation
* 🔍 Missing Skills Detection
* ⚡ Fast API Response
* 🌐 Deployed Backend API

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* Scikit-learn
* NLP (TF-IDF / vectorization)
* PDF parsing libraries

### Frontend

* React (or Vanilla JS depending on your setup)
* HTML / CSS / JavaScript

### Deployment

* Backend: Render
* Frontend: Vercel

---

## ⚠️ Deployment Architecture (IMPORTANT)

This project is split into two parts:

### ✅ Backend (Flask API)

* Hosted on **Render**
* Handles resume parsing, ML model, and scoring

### ✅ Frontend

* Hosted on **Vercel**
* Calls backend API for predictions

> ❌ IMPORTANT: Vercel does NOT directly run full Flask servers with ML models efficiently.
> ✔️ That is why backend is deployed separately on Render.

---

## 🔧 API Usage

### Endpoint:

```
POST /analyze
```

### Example Request:

```json
{
  "resume_text": "...",
  "job_description": "..."
}
```

### Example Response:

```json
{
  "match_score": 82,
  "missing_skills": ["Docker", "AWS"]
}
```

---

## 📦 Installation (Local Setup)

### 1. Clone repo

```bash
git clone https://github.com/your-username/smart-career-ai.git
cd smart-career-ai
```

### 2. Backend setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 3. Frontend setup

```bash
cd frontend
npm install
npm start
```

---

## 🚀 Deployment Guide

### Backend (Render)

1. Push backend folder to GitHub
2. Connect Render
3. Add build command:

   ```bash
   pip install -r requirements.txt
   ```
4. Start command:

   ```bash
   python app.py
   ```

### Frontend (Vercel)

1. Connect GitHub repo
2. Set framework: React / Vite
3. Add backend API URL in `.env`:

   ```env
   REACT_APP_API_URL=https://smart-career-ai.onrender.com
   ```

---

## ❗ Common Issues

### ❌ Vercel deployment fails

* Ensure backend is NOT deployed on Vercel
* Only frontend should be on Vercel

### ❌ API not working

* Check Render backend URL
* Ensure CORS is enabled in Flask

---

## 👨‍💻 Author

Keerthi N M

---

## 📌 License

MIT
