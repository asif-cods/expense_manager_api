from fastapi import FastAPI, HTTPException
from database import get_db
from create_query import  create_table

from dotenv import load_dotenv

# Controllers
from expense_module.expense_controller import expense_controller

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Expense Tracker API with mysql"
)

# if table not exists , it will create 
@app.on_event("startup")
def startup_event():
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

# Expenses module import
app.include_router(expense_controller)