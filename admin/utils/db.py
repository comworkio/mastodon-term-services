import os
import psycopg2

cx = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'])

def get_db_connection():
    return cx

def sql_execute(sql, value):
    cx.execute(sql, (value))
    cx.commit()
