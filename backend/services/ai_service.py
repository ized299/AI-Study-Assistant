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

def generate_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
        }
    )
    return response.text
