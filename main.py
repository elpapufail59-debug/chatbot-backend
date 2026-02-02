from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

openai.api_key = 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

app = FastAPI()

# CORS (OBLIGATORIO para que JS funcione)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Chat(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Welcome"}

@app.post("/chat")
def chat(data: Chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": data.message}
        ]
    )
    return {"reply": response.choices[0].message.content}
