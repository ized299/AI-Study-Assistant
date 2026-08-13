from enum import Enum
from pydantic import BaseModel

class StudyTask(str, Enum):
    explain = "explain"
    quiz = "quiz"
    summarize = "summarize"
    flashcards = "flashcards"

class QuestionRequest(BaseModel):
    question: str
    task: StudyTask

class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str
    explanation: str

class QuizResponse(BaseModel):
    questions: list[QuizQuestion]

class AIResponse(BaseModel):
    question: str
    task: str
    response: str | QuizResponse