import os
from mistralai import Mistral
from dotenv import load_dotenv
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def ask_mistral(prompt):
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)

def ask_groq(prompt):
    response = client.chat.complete(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content