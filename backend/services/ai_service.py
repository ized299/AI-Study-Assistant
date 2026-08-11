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

EXPLAIN_INSTRUCTION = """
Explain the student's topic clearly and simply.
Break difficult concepts into smaller parts.
Use examples where helpful.
Focus on helping the student understand the concept.
"""

QUIZ_INSTRUCTION = """
Create a quiz that helps the student test their understanding.
Use clear questions appropriate for the student's topic.
Include multiple-choice options where appropriate.
Provide the correct answers and brief explanations after the questions.
"""

SUMMARIZE_INSTRUCTION = """
Summarize the student's provided topic or content clearly and concisely.
Focus on the most important ideas and key points.
Do not add unnecessary information that is not present in the student's content.
Organize the summary so it is easy for a student to review.
"""

FLASHCARDS_INSTRUCTION = """
Create study flashcards that help the student review the topic.
Each flashcard should have a clear question or term on the front
and a concise answer or definition on the back.
Focus on important concepts and facts.
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
    return response.text
