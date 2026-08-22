import os
import json
from dotenv import load_dotenv
from google import genai
from ..models import QuizResponse, FlashcardResponse

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

EXPLAIN_INSTRUCTION = """
Explain the student's topic clearly and simply.
Break difficult concepts into smaller parts.
Use examples where helpful.
Focus on helping the student understand the concept.
"""


SUMMARIZE_INSTRUCTION = """
Summarize the student's provided content for quick student revision.

Keep only the most important ideas, facts, definitions, and concepts.
Remove repetition, minor details, and information that is not essential
to understanding the main topic.

The summary should be significantly shorter than the original content.
Aim for approximately 20-30% of the original length when enough content
is provided.

Use short paragraphs or bullet points to make the summary easy to scan.
Do not introduce information that is not present in the student's content.

The goal is to help the student quickly review the material, not to
rewrite the entire content in slightly fewer words.
"""


QUIZ_INSTRUCTION = """
Create a quiz that helps the student test their understanding.

Create 5 multiple-choice questions.

Each question must contain:
- question: the question text
- options: exactly 4 answer choices
- answer: the correct answer
- explanation: a brief explanation of why the answer is correct

Make the questions appropriate for the student's topic and educational level.

Return the quiz as valid JSON with this exact structure:

{
    "questions": [
        {
            "question": "Question text",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "The correct answer",
            "explanation": "Why this answer is correct"
        }
    ]
}

Do not include Markdown code fences or any text outside the JSON.
"""

FLASHCARDS_INSTRUCTION = """
Create study flashcards that help the student review the topic.

Create 5 flashcards.

Each flashcard must contain:
- front: a clear question, term, or concept
- back: a concise answer, definition, or explanation

Focus on important concepts that a student should remember.

Return the flashcards as valid JSON with this exact structure:

{
    "flashcards": [
        {
            "front": "Question or term",
            "back": "Answer or definition"
        }
    ]
}

Do not include Markdown code fences or any text outside the JSON.
"""


TASK_INSTRUCTIONS = {
    "explain": EXPLAIN_INSTRUCTION,
    "quiz": QUIZ_INSTRUCTION,
    "summarize": SUMMARIZE_INSTRUCTION,
    "flashcards": FLASHCARDS_INSTRUCTION,
}

def generate_ai_response(prompt, task):
    task_instruction = TASK_INSTRUCTIONS[task]
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "system_instruction": f"""

            {SYSTEM_INSTRUCTION}
            {task_instruction}

            """
        }
    )
    if task == "quiz":
        quiz_data = json.loads(response.text)
        return QuizResponse(**quiz_data)

    if task == "flashcards":
        flashcard_data = json.loads(response.text)
        return FlashcardResponse(**flashcard_data)
    
    return response.text
