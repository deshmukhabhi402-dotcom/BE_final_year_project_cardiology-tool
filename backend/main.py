from fastapi import FastAPI
from pydantic import BaseModel

from backend.chatbot.conversation import (
    save_message,
    get_history,
    generate_basic_reply
)

app = FastAPI(title="Cardio Companion")


class ChatRequest(BaseModel):
    patient_id: str
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

    # Save patient's message
    save_message(
        request.patient_id,
        "patient",
        request.message
    )

    # Generate temporary companion response
    reply = generate_basic_reply(
        request.patient_name,
        request.message
    )

    # Save bot response
    save_message(
        request.patient_id,
        "companion",
        reply
    )

    return {
        "patient_id": request.patient_id,
        "reply": reply,
        "conversation_length": len(
            get_history(request.patient_id)
        )
    }


@app.get("/chat/history/{patient_id}")
def chat_history(patient_id: str):

    return {
        "patient_id": patient_id,
        "history": get_history(patient_id)
    }