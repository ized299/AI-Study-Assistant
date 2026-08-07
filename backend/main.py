from fastapi import FastAPI

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