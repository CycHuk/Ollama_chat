from ollama_client import model, client
from sockets import message
import db

async def chat(chat_id: str, user_message: str):
    try:
        db.chat.update_chat(chat_id, can_user_write=False)
        db.message.create_message(chat_id, "bot", "Загрузка...")

        stream  = await client.chat(model=model, messages = [
            {
                'role': 'user',
                'content': user_message,
            },
        ], stream=True)

        response = ""

        async for chunk in stream:
            response += chunk['message']['content']
            await message.send_json(chat_id, response, "bot", streaming=True)
            db.message.update_message(chat_id, response)

    except Exception as e:
        print(f"Ошибка генерации ответа: {e}")

    finally:
        print("123")
        db.chat.update_chat(chat_id, can_user_write=True)