from fastapi import APIRouter, WebSocketDisconnect, WebSocket
from typing import Dict, List

router = APIRouter()

active_connections: Dict[str, List[WebSocket]] = {}

@router.websocket("/ws/message/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str):
    await websocket.accept()

    if chat_id not in active_connections:
        active_connections[chat_id] = []

    active_connections[chat_id].append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections[chat_id].remove(websocket)
        if not active_connections[chat_id]:
            del active_connections[chat_id]

async def send_json(chat_id: str, message: str, role: str, streaming: bool = False):
    for websocket in active_connections[chat_id]:
        try:
            await websocket.send_json({
                "role": role,
                "message": message,
                "streaming": streaming
            })
        except:
            active_connections[chat_id].remove(websocket)
