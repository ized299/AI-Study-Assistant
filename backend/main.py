from fastapi import FastAPI
from .models import QuestionRequest
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)
SYSTEM_INSTRUCTION = """
You are an AI Study Assistant.

Your purpose is to help students understand academic concepts clearly.
Explain difficult topics in simple, structured language.
Use examples when they help understanding.
Encourage learning and understanding rather than simply giving answers.
Adapt your explanations to the student's question.
"""

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Study Assistant API!"
    }

@app.get("/about")
def about():
    return {
        "project": "AI Study Assistant",
        "version": "1.0.0",
        "developer": "Iz",
        "status": "Under Development",
    }

@app.get("/info")
def info():
    return {
        "name": "AI Study Assistant",
        "author": "Iz",
        "language": "Python",
        "framework": "FastAPI",
    }

@app.post("/ask-ai")
def ask_ai(request: QuestionRequest):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
        Task: {request.task.value}

        Student's request:
        {request.question}
        """,

        config={
            "system_instruction": SYSTEM_INSTRUCTION,
        }
    )

    return {
        "question": request.question,
        "response": response.text
    }
