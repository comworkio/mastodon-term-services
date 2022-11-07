import os
import psycopg2

_cx = psycopg2.connect(
    host = os.environ['DB_HOST'],
    port = int(os.environ['DB_PORT']),
    database = os.environ['DB_NAME'],
    user = os.environ['DB_USER'],
    password = os.environ['DB_PASSWORD'])

def get_db_connection():
    return _cx

def sql_execute(sql, value):
    cx = get_db_connection()
    cursor = cx.cursor()
    cursor.execute(sql, (value))
    cx.commit()
    cursor.close()
