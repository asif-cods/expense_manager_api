# import mysql.connector
import aiomysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def get_db():
    conn = await aiomysql.connect(
        DB_NAME=os.getenv('DB_NAME'),
        DB_HOST=os.getenv('DB_HOST'),
        DB_PASSWORD=os.getenv('DB_PASSWORD'),
        DB_USER=os.getenv('DB_USER'),
    )
    return conn

