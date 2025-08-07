import os
from dotenv import load_dotenv
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
# Load environment variables from .env file
load_dotenv()

def ask_groq(prompt):
    response = client.chat.complete(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content