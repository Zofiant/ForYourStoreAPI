from fastapi import APIRouter, Depends, Request

from app.cart.repository import CartService
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/cart",
    tags=["Корзины"],
    
)


@router.get("")
async def get_cart(user : Users = Depends(get_current_user)):
    print(user, type(user),user.email)