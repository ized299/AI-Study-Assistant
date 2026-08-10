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