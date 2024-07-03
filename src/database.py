import psycopg2
import os

def connect():
    """Проверка соединения с БД"""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="company",
            user="postgres",
            password="password",
            host="localhost"
        )
        print("Connecting to the PostgreSQL database...")
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print("PostgreSQL database version:", db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == '__main__':
    connect()