from fastapi import FastAPI

from .models import QuestionRequest
from .services.ai_service import generate_ai_response


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
        prompt=f"""
        Task: {request.task.value}

        Student's request:
        {request.question}
        """

        response = generate_ai_response(prompt)
    
        return {
        "question": request.question,
        "response": response
        }
