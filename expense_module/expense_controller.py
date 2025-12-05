from fastapi import APIRouter
from starlette import status
from . import expense_model as dto, expense_service

expense_controller = APIRouter(tags=["Expenses"], prefix="/api/v1/expenses")


@expense_controller.get('', response_model=dto.GetAllExpensesResponseModel, status_code=status.HTTP_200_OK)
def get_all_expenses():
    return expense_service.get_all_expenses()