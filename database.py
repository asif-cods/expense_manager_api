# import mysql.connector
import aiomysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def get_db():
    conn = await aiomysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        port=3306  # default MySQL port
    )
    return conn

