from fastapi import FastAPI, HTTPException
from database import get_db
from models import Expense
from contextlib import asynccontextmanager
from create_query import  create_table
import aiomysql


app = FastAPI(
    title="Expense Tracker API with mysql"
)

# Run create_table() at server startup (correct way)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # his runs before the server starts
    await create_table()
    yield
    # This runs when the server shuts down (optional)
    print("Shutting down...")


# add expenses in  database 
@app.post("/expense")
async def add_expense(expense : Expense):
    conn = await get_db()
    cursor = await conn.cursor()

    query = """
            INSERT INTO expense_tb (name, amount, category, date)
            values (%s, %s, %s,%s) """
    
    await cursor.execute(query, 
                   (expense.name, expense.amount, expense.category, expense.date)
                   )
    await conn.commit()

    new_id = cursor.lastrowid

    await cursor.close()
    conn.close()
    # await conn.wait_closed()

# **expense  - data that came from user 
# .model_dump() converts it to a dictionary for response
    return {"id": new_id, **expense.model_dump()}




# get single  expense
@app.get("/expense/{id}")
async def get_expense(id: int):
    conn = await get_db()
    # cursor = await conn.cursor(dictionary=True) , dictionary=True (not supported by aiomysql)
    cursor = await conn.cursor(aiomysql.DictCursor)

    await cursor.execute("SELECT * FROM expense_tb WHERE id=%s",(id,))
    row = await cursor.fetchone()
    await cursor.close()
    conn.close()
    await conn.wait_closed()

    if not row:
        raise HTTPException(status_code=404, detail="Expense not found")

    return row