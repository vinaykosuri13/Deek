
# ==========================
# Deek API Server
# Version: 1.0
# ==========================

from fastapi import FastAPI
from pydantic import BaseModel

from controller import DeekController


app = FastAPI(
    title="Deek AI",
    version="1.0"
)

controller = DeekController()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def home():

    return {
        "status": "running",
        "name": "Deek AI",
        "version": "1.0"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = controller.process(request.message)

    return ChatResponse(
        reply=answer
    )
