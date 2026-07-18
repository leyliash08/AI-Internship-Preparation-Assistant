# AI Internship Preparation Assistant

## Project Description

AI Internship Preparation Assistant is a full-stack web application that helps students prepare for internships by generating personalized learning plans using OpenAI.

The application analyzes a user's internship goal, identifies the required skills, detects skill gaps, creates a learning plan, and suggests next steps. Every generated analysis is stored in a SQLite database and can be reopened later through the analysis history.

---

## Features

- Generate personalized internship preparation plans using OpenAI
- Identify required technical and soft skills
- Detect current skill gaps
- Generate a structured learning plan
- Suggest next steps for improvement
- Store analyses in a SQLite database
- View and reopen previous analyses
- Refresh analysis history

---

## Technologies

### Frontend

- Vue 3
- Vite
- JavaScript
- CSS

### Backend

- FastAPI
- Python
- OpenAI API
- SQLAlchemy
- SQLite

---

## Project Structure

```text
AI-Internship-Preparation-Assistant/
│
├── backend/
│   ├── .env # OpenAI API key
│   ├── database.py # Database configuration and SQLAlchemy setup
│   ├── internship_requests.db # SQLite database
│   ├── main.py # FastAPI application and API endpoints
│   └── requirements.txt # Python dependencies
│
├── docs/
│   └── journal.md # Development journal Day 1- Day 5
│
├── frontend/
│   ├── public/ # Static assets
│   ├── src/
│   │   ├── App.vue # Main Vue application component
│   │   └── main.js # Vue application entry point
│   ├── package.json # Frontend dependencies 
│   ├── vite.config.js # Vite configuration
│   └── README.md 
│
├── .gitignore
└── README.md # Project documentation
```

## Installation

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Future Improvements

- User authentication
- Export learning plans as PDF
- Support for multiple languages
- Progress tracking
- Favorite analyses

---

## Author

Leyli Ashyrova