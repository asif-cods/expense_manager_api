import aiomysql
from database import get_db


async def  create_table():
    conn = await get_db()
    cursor =await conn.cursor()

    await cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS expense_tb (id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            amount FLOAT NOT NULL,
            category VARCHAR(50) NOT NULL,
            date VARCHAR(20) NOT NULL)
        """
    )
    await conn.commit()
    await cursor.close()
    conn.close()