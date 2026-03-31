# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class Message(BaseModel):
    text: str

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.post("/chat")
async def chat(message: Message):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            # "model": "openrouter/free"
            "model": "moonshotai/kimi-k2.5",
            "messages": [
                {"role": "user", "content": message.text}
            ]
        }
    )

    data = response.json()

    return {
        "reply": data["choices"][0]["message"]["content"]
    }
