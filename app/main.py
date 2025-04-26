from fastapi import FastAPI
import os

# Only initialize database-related stuff if not building docs
if os.getenv('GENERATING_DOCS') != '1':
    from app.products.router import router as router_products
    from app.users.router import router as router_users
    from app.cart.router import router as router_cart
    from app.orders.router import router as router_orders

app = FastAPI()

if os.getenv('GENERATING_DOCS') != '1':
    app.include_router(router_users)
    app.include_router(router_products)
    app.include_router(router_cart)
    app.include_router(router_orders)