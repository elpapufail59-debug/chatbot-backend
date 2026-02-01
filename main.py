from fastapi import FastAPI
from pydantic import BaseModel

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
