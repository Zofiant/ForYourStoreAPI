from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.products.models import Products
from app.products.repository import ProductRepository
from app.products.schemas import SProduct

router = APIRouter(
    prefix="/products",
    tags=["Продукты"],
    
)


@router.get("")
async def get_products():
    return await ProductRepository.find_all()

   

