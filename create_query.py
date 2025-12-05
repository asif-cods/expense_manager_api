from database import get_db



def  create_table():
    conn = get_db()
    cursor =conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS expenses
            (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            amount FLOAT NOT NULL,
            category VARCHAR(50) NOT NULL,
            date VARCHAR(20) NOT NULL
            )
        """
    )
    conn.commit()
    cursor.close()
    conn.close()