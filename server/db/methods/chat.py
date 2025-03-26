from db.connection import connection
from db.models import Chat
from sockets import chat as chat_socket


def create_chat():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO `chats` (title) VALUES ('Новый чат');")

        connection.commit()

    with connection.cursor() as cursor:

        cursor.execute("SELECT * FROM chats ORDER BY created_at DESC LIMIT 1;")
        chat = cursor.fetchone()

        return chat


def get_chat(chat_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `chats` WHERE `id` = %s;", (chat_id,))
        chat = cursor.fetchone()

        return chat


async def update_chat(chat_id, title=None, can_user_write=None, response_by=None):
    with connection.cursor() as cursor:
        update_fields = []
        update_values = []

        if title is not None:
            update_fields.append("title = %s")
            update_values.append(title)

        if can_user_write is not None:
            update_fields.append("can_user_write = %s")
            update_values.append(can_user_write)

        if response_by is not None:
            update_fields.append("response_by = %s")
            update_values.append(response_by)

        if update_fields:
            update_values.append(chat_id)

            update_query = f"UPDATE `chats` SET {', '.join(update_fields)} WHERE `id` = %s"
            cursor.execute(update_query, tuple(update_values))
            connection.commit()

        cursor.execute("SELECT * FROM `chats` WHERE `id` = %s;", (chat_id,))
        chat = cursor.fetchone()

        chat = Chat(**chat).to_dict()
        print(chat)
        await chat_socket.send_json(chat['id'], chat)



def delete_chat(chat_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `chats` WHERE `id` = %s;", (chat_id,))
        connection.commit()

