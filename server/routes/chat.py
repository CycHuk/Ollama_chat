from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models import Chat
import db


class ChatRequest(BaseModel):
    id: str

router = APIRouter(tags=["Chat"])

@router.post("/chat/create")
def create_chat():
    try:
        chat = db.chat.create_chat()

        return Chat(**chat).to_dict()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat")
def get_chat(request: ChatRequest):
    try:
        chat_id = request.id
        chat = db.chat.get_chat(chat_id)

        if not chat:
            raise HTTPException(status_code=404, detail="Чат не найден")

        return Chat(**chat).to_dict()

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/chat")
def get_chat(request: ChatRequest):
    try:
        chat_id = request.id
        db.chat.delete_chat(chat_id)

        return "Чат удален"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
