# ==========================
# Deek API Server
# Version: 2.0
# ==========================

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from controller import DeekController

app = FastAPI(
    title="Deek AI",
    version="2.0"
)

controller = DeekController()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    type: str
    reply: Optional[str] = None
    action: Optional[str] = None
    contact: Optional[str] = None
    destination: Optional[str] = None
    site: Optional[str] = None
    app: Optional[str] = None
    state: Optional[str] = None
    time: Optional[str] = None
    text: Optional[str] = None


@app.get("/")
def home():
    return {
        "status": "running",
        "name": "Deek AI",
        "version": "2.0"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = controller.process(request.message)

    if isinstance(result, dict):
        return ChatResponse(
            type="action",
            action=result.get("action"),
            contact=result.get("contact"),
            destination=result.get("destination"),
            site=result.get("site"),
            app=result.get("app"),
            state=result.get("state"),
            time=result.get("time"),
            text=result.get("text")
        )

    return ChatResponse(
        type="chat",
        reply=result
    )
