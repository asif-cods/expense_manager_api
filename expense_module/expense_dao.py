from database import get_db
from mysql.connector import MySQLConnection
from fastapi import HTTPException

db: MySQLConnection = get_db()

def get_all_expenses():
    try:
        if not db.is_connected():
            raise HTTPException(detail="Database not connected")
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, amount, category, date AS createdDate FROM expenses")
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise e
    finally:
        if cursor:
            cursor.close()