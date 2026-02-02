from fastapi import FastAPI
from pydantic import BaseModel
import openai

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
openai.api_key=

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Servidor IA activo"}

@app.post("/chat")
def chat(msg: Message):
    return {
        "reply": f"Recibí tu mensaje: {msg.message}"
    }
