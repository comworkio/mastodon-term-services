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

def sql_exec(sql):
    cx = get_db_connection()
    cursor = cx.cursor()
    cursor.execute(sql)
    cx.commit()
    cursor.close()

def sql_exec_values(sql, values):
    cx = get_db_connection()
    cursor = cx.cursor()
    cursor.execute(sql, values)
    cx.commit()
    cursor.close()

def sql_exec_value(sql, value):
    sql_exec_values(sql, (value,))
