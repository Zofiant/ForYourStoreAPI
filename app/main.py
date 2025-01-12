from typing import Annotated

from fastapi import FastAPI, Query, Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.products.router import router as router_products
from app.users.router import router as router_users
from app.cart.router import router as router_cart

app = FastAPI()

app.include_router(router_users)
app.include_router(router_products)
app.include_router(router_cart)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")





# @app.get("/products/{product_id}")
# def get_product(
#         product_id:int,
#         price:int,
#         stars:int | None = Query(default = None,ge=1, le=5),
#         description:str | None = None
# ):
#     return product_id, price, stars,description

# @app.get("/products/")
# def get_product(product_id:int, price:int, description:str | None = None):
#     return product_id, price, description


# @app.post("/cart")
# def add_to_cart(cart_item: SProduct):
#     pass





