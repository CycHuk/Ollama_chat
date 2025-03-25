from db.connection import connection


def create_chat():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO `chats` () VALUES ();")

        cursor.execute("SELECT * FROM `chats` WHERE `id` = LAST_INSERT_ID();")
        chat = cursor.fetchone()
        connection.commit()

        return chat

def get_chat(chat_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `chats` WHERE `id` = %s;", (chat_id,))
        chat = cursor.fetchone()

        return chat

def delete_chat(chat_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `chats` WHERE `id` = %s;", (chat_id,))
        connection.commit()