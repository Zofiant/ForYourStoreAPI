from fastapi import FastAPI


from app.products.router import router as router_products
from app.users.router import router as router_users
from app.cart.router import router as router_cart
from app.orders.router import router as router_orders

app = FastAPI()


app.include_router(router_users)
app.include_router(router_products)
app.include_router(router_cart)
app.include_router(router_orders)