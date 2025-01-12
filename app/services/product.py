from app.repository.base import BaseRepository
from app.products.models import Products
from app.products.schemas import SProduct
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

class ProductService:
    def __init__(self):
        self.products = []

    def create_product(self, s_product: SProduct) -> SProduct:
        new_product = SProduct(
            product_id=len(self.products) + 1,
            **s_product.dict(exclude={"product_id"})
        )
        self.products.append(new_product)
        return new_product

    def get_all_products(self) -> List[SProduct]:
        return self.products

    def get_product_by_id(self, product_id: int) -> SProduct:
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise HTTPException(status_code=404, detail="Продукт не найден")

    def update_product(self, product_id: int, s_product: SProduct) -> SProduct:
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                updated_product = SProduct(
                    **s_product.dict(exclude_unset=True),
                    product_id=product_id
                )
                self.products[i] = updated_product
                return updated_product
        raise HTTPException(status_code=404, detail="Продукт не найден")

    def delete_product(self, product_id: int) -> bool:
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                return True
        return False