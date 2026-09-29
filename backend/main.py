from fastapi import FastAPI
from pydantic import BaseModel

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
        "bot": f"Hi {request.patient_name}, thanks for checking in. You said: '{request.message}'. I'm here with you."
    }