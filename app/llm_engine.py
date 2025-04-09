import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages = [
            {"role": "system", "content": "You are a senior data scientist. "},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']