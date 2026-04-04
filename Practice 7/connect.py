import psycopg2
from config import parameters

def get_connection():
    try:
        # Unpacking dictionary params directly in arguments of function
        conn = psycopg2.connect(**parameters)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при подключении к PostgreSQL: {error}")
        return None
