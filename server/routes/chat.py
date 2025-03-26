from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models import Chat
from typing import List 
import db


class ChatRequest(BaseModel):
    id: str

class ChatsRequest(BaseModel):
    id: List[str]

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
    
@router.post("/chats")
def get_chat(request: ChatsRequest):
    try:
        ids = request.id  # Здесь предположим, что id - это список строк
        chat_list = []  # Создаем пустой список для чатов
        for id in ids:
            chat = db.chat.get_chat(id)  # Получаем чат по id
            if not chat:  # Если чат не найден, пропускаем
                continue
            chat_list.append(Chat(**chat).to_dict())  # Преобразуем в объект Chat и добавляем в список

        return chat_list  # Возвращаем список чатов
    except Exception as e:
        # Обработка исключений
        return {"error": str(e)}


@router.delete("/chat")
def get_chat(request: ChatRequest):
    try:
        chat_id = request.id
        db.chat.delete_chat(chat_id)

        return "Чат удален"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
