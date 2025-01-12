from typing import Annotated

from fastapi import FastAPI, Query, Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
from io import BytesIO
import io

import pytest
import matplotlib.pyplot as plt
from faker import Faker
from app.users.schemas import SUserRegister
from app.users.router import register_user

from app.products.router import router as router_products
from app.users.router import router as router_users
from app.cart.router import router as router_cart
from app.orders.router import router as router_orders


app = FastAPI()



# Инициализация Faker
fake = Faker()

def generate_fake_users():
    users = [
        SUserRegister(
            name=fake.first_name(),
            surname=fake.last_name(),
            email=fake.email(),
            password=fake.password()
        ) for _ in range(100)
    ]
    return users

@app.get("/plot")
async def test_user_distribution():

    users = generate_fake_users()
    surnames = [user.surname for user in users]


    surname_counts = {surname: surnames.count(surname) for surname in set(surnames)}

    plt.figure(figsize=(25, 6))
    plt.bar(surname_counts.keys(), surname_counts.values())
    plt.xlabel('Фамилия')
    plt.ylabel('Количество пользователей')
    plt.title('Распределение пользователей по фамилиям')
    plt.xticks(rotation=45)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  
    return StreamingResponse(buf, media_type="image/png")

app.include_router(router_users)
app.include_router(router_products)
app.include_router(router_cart)
app.include_router(router_orders)





