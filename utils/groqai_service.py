from groq import Groq
import os

def ask_groq(prompt_text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",  # or your preferred model
        messages=[
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message.content