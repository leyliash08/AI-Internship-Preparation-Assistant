import json
import os

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

    return{
        'internship_goal': request.internship_goal,
        'required_skills': result.get('required_skills', []),
        'learning_plan': result.get('learning_plan', []),
        'skill_gaps': result.get('skill_gaps', []),
        'next_steps': result.get('next_steps', []),
    }