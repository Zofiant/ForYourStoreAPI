from fastapi import APIRouter, Depends, Request


from app.cart.schemas import SDelivery
from app.products.schemas import SProductAdd
from app.services.cart import validate_delivery
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.cart.repository import CartRepository 
from app.orders.models import Order_delivery


router = APIRouter(
    prefix="/cart",
    tags=["Корзины"],
    
)


@router.post("/add")
async def add_cart_item(product_items: SProductAdd , current_user: Users = Depends(get_current_user)):
    print(current_user.user_id)
    return await CartRepository.add(product_items.product_id, product_items.quantity , current_user.user_id)
    
    
@router.get("/me")
async def get_cart(current_user: Users = Depends(get_current_user)):
    return await CartRepository.get_cart(current_user.user_id)


@router.patch("/me/deleteone/{cart_item_id}")
async def delete_item_one(cart_item_id : int,current_user: Users = Depends(get_current_user)):
    await CartRepository.delete_item_one(cart_item_id,current_user.user_id)

@router.delete("/me/deleteall/{cart_item_id}")
async def delete_item_all(cart_item_id : int,current_user: Users = Depends(get_current_user)):
    await CartRepository.delete_item_all(cart_item_id,current_user.user_id)


@router.post("/me/create_order")
async def create_order( delivery_info: SDelivery = Depends(validate_delivery), current_user: Users = Depends(get_current_user)):

    if delivery_info.order_delivery == Order_delivery.Courier:
        address = delivery_info.address_courier
    else:
        address = delivery_info.address_pickup

    result =  await CartRepository.create_order(address,delivery_info.order_delivery, current_user.user_id)
    await CartRepository.clear_cart(current_user.user_id)
    return result
