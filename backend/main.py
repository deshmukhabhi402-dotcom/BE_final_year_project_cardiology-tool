from fastapi import FastAPI
from pydantic import BaseModel

from backend.chatbot.conversation import companion_reply

app = FastAPI(title="Cardio Companion")


class ChatRequest(BaseModel):
    patient_name: str
    message: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Cardio Companion backend is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "patient": request.patient_name,
        "bot": companion_reply(request.patient_name, request.message)
    }