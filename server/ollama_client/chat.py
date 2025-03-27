import time

from ollama_client import model, client
from sockets import message
import db

async def chat(chat_id: str, user_message: str):
    try:
        load = """
             
<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span>

<style>
    .dot {
        animation: blink 1.5s infinite;
        font-size: 24px;
    }
    .dot:nth-of-type(1) { animation-delay: 0s; }
    .dot:nth-of-type(2) { animation-delay: 0.3s; }
    .dot:nth-of-type(3) { animation-delay: 0.6s; }

    @keyframes blink {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
</style>



        """

        db.chat.update_chat(chat_id, can_user_write=False)
        db.message.create_message(chat_id, "bot",  load)
        await message.send_json(chat_id, load, "bot", streaming=True)
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