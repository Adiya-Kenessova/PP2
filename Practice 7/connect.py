# connect.py
import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="phonebook_db",
            user="postgres",
            password="5432",
            port="5432"
        )
        print("Connection successful!")
        return conn
    except Exception as e:
        print("Ошибка подключения:", e)
        return None
