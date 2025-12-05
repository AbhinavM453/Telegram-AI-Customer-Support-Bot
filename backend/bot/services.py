from groq import Groq
import os
from backend.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_ai_response(user_message):
    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful customer support AI bot."},
            {"role": "user", "content": user_message}
        ]
    )
    return chat_completion.choices[0].message.content
