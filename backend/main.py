import json
import os

from database import Analysis, SessionLocal
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise RuntimeError('OPENAI_API_KEY is not configured.')
client = OpenAI(api_key=api_key)

app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InternshipRequest(BaseModel):
    internship_goal: str

@app.get("/")
def root():
    return {"message": "AI Internship Preparation Assistant Backend is running!"}

@app.post("/analyze")
def analyze_internship_request(request: InternshipRequest):
    # Here you can implement the logic to analyze the internship request
    # For now, we will just return the received request for demonstration purposes
    prompt = f"""
    You are an internship preparation assistant.

    Analyze the following internship goal:
    {request.internship_goal}

    Return only valid JSON with the exact structure:
    {{
       "required_skills": [],
        "learning_plan": [],
        "skill_gaps": [],
        "next_steps": [], 
    }}

    Each field must contain short, practical items.
    Do not include markdown.
    Do not include any text outside the JSON.
    """
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    result = json.loads(response.output_text)

   
    required_skills = result.get('required_skills', [])
    learning_plan = result.get('learning_plan', [])
    skill_gaps = result.get('skill_gaps', [])
    next_steps = result.get('next_steps', [])

    database = SessionLocal()

    try:
        analysis = Analysis(
            internship_goal=request.internship_goal,
            required_skills=json.dumps(required_skills),
            learning_plan=json.dumps(learning_plan),
            skill_gaps=json.dumps(skill_gaps),
            next_steps=json.dumps(next_steps),
        )
        database.add(analysis)
        database.commit()
        database.refresh(analysis)
    
    finally:
        database.close()

    return {
        'id': analysis.id,
        'internship_goal': request.internship_goal,
        'required_skills': required_skills,
        'learning_plan': learning_plan,
        'skill_gaps': skill_gaps,
        'next_steps': next_steps,
        'created_at': analysis.created_at,
    }

@app.get('/analyses')
def get_analyses():
    database = SessionLocal()

    try:
        analyses = (
            database.query(Analysis)
            .order_by(Analysis.created_at.desc())
            .all()
        )

        return [
            {
                'id': analysis.id,
                'internship_goal': analysis.internship_goal,
                'required_skills': json.loads(analysis.required_skills),
                'learning_plan': json.loads(analysis.learning_plan),
                'skill_gaps': json.loads(analysis.skill_gaps),
                'next_steps': json.loads(analysis.next_steps),
                'created_at': analysis.created_at,
            }
            for analysis in analyses
        ]
    finally:
        database.close()