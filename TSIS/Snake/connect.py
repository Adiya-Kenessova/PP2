import psycopg2

def get_connect():
    try:
        conn = psycopg2.connect(
            dbname="snake_db",
            user="postgres",
            password="5432",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None