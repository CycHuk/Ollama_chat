from fastapi import FastAPI
from routes import chat, message
from sockets import message as ws_message, chat as ws_chat

app = FastAPI()

app.include_router(chat.router)
app.include_router(message.router)
app.include_router(ws_message.router)
app.include_router(ws_chat.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)