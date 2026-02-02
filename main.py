from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# 🔥 CORS BIEN CONFIGURADO
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← ESTO ES CLAVE
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mensaje(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Welcome"}

@app.post("/chat")
def chat(mensaje: Mensaje):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mensaje.message}
        ]
    )
    return {"reply": response.choices[0].message.content}
