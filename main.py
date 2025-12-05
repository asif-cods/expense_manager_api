from fastapi import FastAPI, HTTPException
from database import get_db
from create_query import  create_table

app = FastAPI(
    title="Expense Tracker API with mysql"
)

# if table not exists , it will create 
create_table()


# add expenses in  database 
@app.post("/expense")
async def add_expense(expense : dict):
    conn = await get_db()
    cursor = await conn.cursor()

    query = """
            INSERT INTO expense_tb (name, amount, category, date)
            values (%s, %s, %s,%s) """
    
    cursor.execute(query, 
                   (expense["name"], expense['amount'], expense['category'], expense['date'])
                   )
    await conn.commite()

    new_id = cursor.lastrowid

    await cursor.close()
    conn.close()
# **expense  - data that came from user 
    return {"id": new_id, **expense}




# get single  expense
@app.get("/expense/{id}")
async def get_expense(id: int):
    conn = await get_db()
    cursor = await conn.cursor(dictionary=True)

    await cursor.execute("SELECT * FROM expense_tb WHERE id=%s",(id,))
    row = await cursor.fetchone()
    await cursor.close()
    conn.close()

    if not row:
        raise HTTPException(status_code= 404, detail="Expense not found")

    return row