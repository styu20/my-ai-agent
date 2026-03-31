# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":message.text}]
    )
    return {"reply": response.choices[0].message.content}
