from . import expense_dao

def get_all_expenses():
    try:
        result = expense_dao.get_all_expenses()
        return {
            "data": result,
            "message": "Get all expenses success",
            "statusCode": 200
        }
    except Exception as e:
        raise e