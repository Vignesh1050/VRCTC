from db import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute()
    cursor.execute()
    cursor.execute()
    conn.commit()
    conn.close()
