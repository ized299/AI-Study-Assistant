from fastapi import FastAPI

from .models import QuestionRequest, AIResponse
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

@app.post("/ask-ai", response_model=AIResponse)
def ask_ai(request: QuestionRequest):
        prompt=f"""
        Task: {request.task.value}

        Student's request:
        {request.question}
        """

        response = generate_ai_response(prompt, request.task.value)
    
        return {
        "question": request.question,
        "task": request.task.value,
        "response": response
        }
