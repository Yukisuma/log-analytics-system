import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="logs_db",
        user="postgres",
        password="2005"
    )