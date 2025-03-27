from db.connection import connection


def create_message(chat_id, writer, message):
    with connection.cursor() as cursor:
        insert_query = "INSERT INTO messages (chat_id, writer, message) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (chat_id, writer, message))
        connection.commit()

def update_message(chat_id, new_message):
    with connection.cursor() as cursor:
        update_query = """
        UPDATE messages 
        SET message = %s, created_at = CURRENT_TIMESTAMP 
        WHERE chat_id = %s AND writer = 'bot' 
        ORDER BY created_at DESC 
        LIMIT 1;
        """
        cursor.execute(update_query, (new_message, chat_id))
        connection.commit()


def get_messages(chat_id, limit=10):
    with connection.cursor() as cursor:
        select_query = "SELECT * FROM messages WHERE chat_id = %s ORDER BY created_at DESC LIMIT %s"
        cursor.execute(select_query, (chat_id, limit))
        result = cursor.fetchall()

        return result[::-1]