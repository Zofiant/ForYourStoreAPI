from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.database import async_session_maker
from app.products.models import Products
from app.products.repository import ProductRepository
from app.products.schemas import SProduct
from app.users.dependencies import get_current_seller_user
from app.users.models import Users

router = APIRouter(
    prefix="/products",
    tags=["Продукты"],
    
)

@router.get("")
async def get_product_all():
    return await ProductRepository.find_all()

@router.get("/{product_id}")
async def get_product(product_id: int):
    return await ProductRepository.find_all(product_id = product_id)
   
@router.post("/create")
async def create_new_product(product_data : SProduct, current_user: Users = Depends(get_current_seller_user)):
    await ProductRepository.add(
        name = product_data.name, 
        price = product_data.price, 
        quantity = product_data.quantity,
        ingredients = product_data.ingredients,
        nutrition = product_data.nutrition,
        description = product_data.description,
        stars = product_data.stars,
        image_id = product_data.image_id
        )

@router.put("/change/{product_id}")
async def change_product(product_id : int,product_data : SProduct, current_user: Users = Depends(get_current_seller_user)):
    return await ProductRepository.update_product(
        product_id = product_id,
        name = product_data.name, 
        price = product_data.price, 
        quantity = product_data.quantity,
        ingredients = product_data.ingredients,
        nutrition = product_data.nutrition,
        description = product_data.description,
        stars = product_data.stars,
        image_id = product_data.image_id
    )
    
@router.delete("/delete/{product_id}")
async def delete_product(product_id:int, current_user: Users = Depends(get_current_seller_user)):
    return await ProductRepository.delete_product(product_id)
     