from pydantic import BaseModel

class ExpenseResponseModel(BaseModel):
    id : int
    name : str
    amount : int
    category : str
    createdDate : str

class GetAllExpensesResponseModel(BaseModel):
    data : list[ExpenseResponseModel]
    message : str
    statusCode : int