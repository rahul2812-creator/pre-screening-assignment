import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:rahul123@db:5432/database")

def get_db_connection():
    return psycopg2.connect(
        dbname="database",
        user="postgres",
        password="rahul123",
        host="db",
        port="5432"
    )

