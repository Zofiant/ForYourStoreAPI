from fastapi import FastAPI


from app.products.router import router as router_products
from app.users.router import router as router_users
from app.cart.router import router as router_cart
from app.orders.router import router as router_orders

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_users)
app.include_router(router_products)
app.include_router(router_cart)
app.include_router(router_orders)