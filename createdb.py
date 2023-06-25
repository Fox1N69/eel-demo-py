import sqlite3 as sql
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
        print("connect database ok...")
    except Error as er:
        print(er)
    finally:
        if conn: 
            conn.close()


if __name__ == '__main__':
    create_connection(r'database/storage.db')