from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import Response
from pydantic import BaseModel
import asyncio

from ollama_client import chat as send_chat
from sockets import message as ws_message
import db

class ChatRequest(BaseModel):
    id: str

class MessageRequest(BaseModel):
    id: str
    message: str

router = APIRouter(tags=["Messages"])

@router.post("/messages")
def get_messages(request: ChatRequest):
    try:
        chat_id = request.id
        chat = db.chat.get_chat(chat_id)

        if not chat["id"]:
            raise HTTPException(status_code=400, detail="Чат не найден")

        messages = db.message.get_messages(chat["id"], 20)
        return messages

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/messages/create")
def create_messages(request: MessageRequest, background_tasks: BackgroundTasks):
    try:
        chat_id = request.id
        chat = db.chat.get_chat(chat_id)

        if not chat["id"]:
            raise HTTPException(status_code=400, detail="Чат не найден")

        if not chat["can_user_write"]:
            raise HTTPException(status_code=400, detail="Дождитесь ответа")

        message = request.message

        background_tasks.add_task(ws_message.send_json, chat_id, message, "user")
        db.message.create_message(chat["id"], "user", message)

        if chat["response_by"] == "bot":
            background_tasks.add_task(send_chat, chat["id"], message)

        return Response(status_code=200)

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))