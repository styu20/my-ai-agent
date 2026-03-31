# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    return {"reply": "Hello! I would answer using OpenAI if I had a key."}
