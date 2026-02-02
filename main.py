from fastapi import FastAPI
from pydantic import BaseModel
import openai  # Librería OpenAI

# Tu API Key de OpenAI
openai.api_key = "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"

app = FastAPI()

# Clase para recibir mensajes
class Mensaje(BaseModel):
    message: str

# Ruta POST /chat
@app.post("/chat")
def chat(mensaje: Mensaje):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje.message}]
    )
    return {"reply": respuesta.choices[0].message.content}
