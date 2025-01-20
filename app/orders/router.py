from typing import Annotated
from fastapi import APIRouter, Depends, Query
from app.orders.models import Order_status
from app.orders.repository import OrderRepository
from app.users.models import Users
from app.orders.models import Order_status
from app.users.dependencies import get_current_user
router = APIRouter(
    prefix="/order",
    tags=["Заказы"],
)

    
@router.get("/user/orders")
async def get_order(current_user: Users = Depends(get_current_user)):
    return await OrderRepository.get_order(current_user.user_id)
    
@router.get("/user/orders/order_items")
async def get_order(current_user: Users = Depends(get_current_user)):
    return await OrderRepository.get_order_items(current_user.user_id)

@router.patch("/change/{order_id}")
async def change_order_status(order_id : int,choice: Annotated[Order_status, Query()]):

    choice_string = choice.value
    print(choice_string)
    await OrderRepository.update(choice_string, order_id)
    
    