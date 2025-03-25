from ollama_client import model, client
from sockets import message
import db


async def chat(chat_id: str, user_message: str):
    try:
        await db.chat.update_chat(chat_id, can_user_write=False)
        stream  = client.chat(model=model, messages = [
            {
                'role': 'user',
                'content': user_message,
            },
        ], stream=True)

        response = ""

        for chunk in stream:
            response += chunk['message']['content']
            await message.send_json(chat_id, response, "bot", streaming=True)

        db.message.create_message(chat_id, "bot", response)
        await db.chat.update_chat(chat_id, can_user_write=True)

    except Exception as e:
        print(f"Ошибка генерации ответа: {e}")