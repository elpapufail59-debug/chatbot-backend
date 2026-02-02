from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

# 🔑 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"

# En Render la pones como Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# ✅ CORS (OBLIGATORIO para HTML + JS en celular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Modelo del mensaje
class Mensaje(BaseModel):
    message: str

# 🟢 Ruta de prueba (Welcome)
@app.get("/")
def root():
    return {"message": "Welcome"}

# 🤖 Chatbot
@app.post("/chat")
def chat(mensaje: Mensaje):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente inteligente y útil."},
            {"role": "user", "content": mensaje.message}
        ]
    )

    return {
        "reply": respuesta.choices[0].message.content
    }
