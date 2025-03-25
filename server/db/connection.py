from .config import host, port, user, password, db_name
import pymysql


connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)