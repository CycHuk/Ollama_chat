from db.connection import connection


def create_message(chat_id, writer, message):
    with connection.cursor() as cursor:
        insert_query = "INSERT INTO messages (chat_id, writer, message) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (chat_id, writer, message))
        connection.commit()

def get_messages(chat_id):
    with connection.cursor() as cursor:
        select_query = "SELECT * FROM messages WHERE chat_id = %s ORDER BY created_at;"
        cursor.execute(select_query, (chat_id,))
        result = cursor.fetchall()
        return result