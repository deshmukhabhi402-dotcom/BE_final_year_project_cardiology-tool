from fastapi import FastAPI

app = FastAPI(title="Cardio Companion")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Cardio Companion backend is running."
    }