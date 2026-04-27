import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const API = "http://127.0.0.1:5000";

function App() {
  const [resume, setResume] = useState("");
  const [jobDesc, setJobDesc] = useState("");

  const [atsScore, setAtsScore] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [skills, setSkills] = useState([]);

  const getATS = async () => {
    const res = await axios.post(`${API}/resume-score`, {
      resume,
      job_description: jobDesc,
    });
    setAtsScore(res.data.ats_score);
  };

  const getJobs = async () => {
    const res = await axios.post(`${API}/recommend-jobs`, { resume });
    setJobs(res.data.recommended_jobs);
  };

  const getSkillGap = async () => {
    const res = await axios.post(`${API}/skill-gap`, { resume });
    setSkills(res.data.skill_gap_analysis);
  };

  return (
    <div className="dashboard">

      {/* LEFT PANEL */}
      <div className="left">
        <h2>🚀 Resume Analyzer</h2>

        <textarea
          placeholder="Paste Resume"
          onChange={(e) => setResume(e.target.value)}
        />

        <textarea
          placeholder="Paste Job Description"
          onChange={(e) => setJobDesc(e.target.value)}
        />

        <button onClick={getATS}>Check ATS Score</button>
        <button onClick={getJobs}>Get Jobs</button>
        <button onClick={getSkillGap}>Skill Gap</button>
      </div>

      {/* RIGHT PANEL */}
      <div className="right">

        {/* ATS SCORE */}
        {atsScore !== null && (
          <div className="card score">
            <h2>ATS Score</h2>
            <div className="circle">
              {atsScore}%
            </div>
          </div>
        )}

        {/* JOBS */}
        {jobs.length > 0 && (
          <div className="section">
            <h2>💼 Recommended Jobs</h2>
            {jobs.map((job, i) => (
              <div className="jobCard" key={i}>
                <h3>{job.title}</h3>
                <span>{job.match_score}% Match</span>
              </div>
            ))}
          </div>
        )}

        {/* SKILL GAP */}
        {skills.length > 0 && (
          <div className="section">
            <h2>🧠 Skill Gap Analysis</h2>

            {skills.map((s, i) => (
              <div className="skillCard" key={i}>
                <h3>{s.job_title}</h3>

                <p>
                  <b>Matched:</b>{" "}
                  {s.matched_skills.map((sk, idx) => (
                    <span className="green" key={idx}>{sk} </span>
                  ))}
                </p>

                <p>
                  <b>Missing:</b>{" "}
                  {s.missing_skills.map((sk, idx) => (
                    <span className="red" key={idx}>{sk} </span>
                  ))}
                </p>
              </div>
            ))}
          </div>
        )}

      </div>
    </div>
  );
}

export default App;